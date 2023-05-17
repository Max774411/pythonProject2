from tkinter import Tk, Canvas, Menu, filedialog
import json


def neightbour(row, col, shape, t):
    # print(row, col, shape, t)
    res = [(row, col, (t + 1) % 2)]
    if shape == 0 and t == 0:
        res.append((row - 1, col, 1))
        s = board[row][col + 1][0]
        res.append((row, col + 1, (s + 1) % 2))
    if shape == 0 and t == 1:
        res.append((row + 1, col, 0))
        s = board[row][col - 1][0]
        res.append((row, col - 1, s))
    if shape == 1 and t == 0:
        res.append((row - 1, col, 1))
        s = board[row][col - 1][0]
        res.append((row, col - 1, s))
    if shape == 1 and t == 1:
        res.append((row + 1, col, 0))
        s = board[row][col + 1][0]
        res.append((row, col + 1, (s + 1) % 2))
    return res


def draw():
    fnt = ('Helvetica 15 bold')
    canvas.delete("all")

    for i in range(n):
        for j in range(m):
            color1 = colors[board[i][j][1]]
            color2 = colors[board[i][j][2]]
            ar1 = board[i][j][3]
            ar2 = board[i][j][4]
            shape = board[i][j][0]
            if shape == 0:
                canvas.create_polygon(j * w, i * w, (j + 1) * w, (i + 1) * w, (j + 1) * w, i * w, fill=color1,
                                      outline=color1)

                canvas.create_polygon(j * w, (i + 1) * w, (j + 1) * w, (i + 1) * w, j * w, i * w, fill=color2,
                                      outline=color2)
                # canvas.create_text(j * w + int(w * 0.75), i * w + int(w * 0.375), text=str(ar1), fill="black", font=fnt)
                # canvas.create_text(j * w + int(w * 0.375), i * w + int(w * 0.75), text=str(ar2), fill="black", font=fnt)
            if shape == 1:
                canvas.create_polygon(j * w, (i + 1) * w, (j + 1) * w, i * w, j * w, i * w, fill=color1,
                                      outline=color1)
                canvas.create_polygon((j + 1) * w, i * w, (j + 1) * w, (i + 1) * w, j * w, (i + 1) * w,
                                      fill=color2, outline=color2)
                # canvas.create_text(j * w + int(w * 0.375), i * w + int(w * 0.375), text=str(ar1), fill="black", font=fnt)
                # canvas.create_text(j * w + int(w * 0.75), i * w + int(w * 0.75), text=str(ar2), fill="black", font=fnt)
            if board[i][j][3] != board[i][j][4]:  # диагональ
                if shape == 0:
                    canvas.create_line((j + 1) * w, (i + 1) * w, j * w, i * w, fill='black', width=3)
                if shape == 1:
                    canvas.create_line(j * w, (i + 1) * w, (j + 1) * w, i * w, fill='black', width=3)
            # левая сторона
            if board[i][j][4 - shape] != board[i][j - 1][3 + board[i][j - 1][0]]:
                canvas.create_line(j * w, i * w, j * w, (i + 1) * w, fill='black', width=3)
            # верхняя сторона
            if board[i][j][3] != board[i - 1][j][4]:
                canvas.create_line(j * w, i * w, (j + 1) * w, i * w, fill='black', width=3)
    canvas.create_rectangle(1, 1, n * w + 1, m * w + 1, width=3, outline="black")







def open_file():
    global board
    filename = filedialog.askopenfilename(title="Открыть файл", initialdir=".")
    if filename:
        with open(filename, "r") as read_file:
            board = json.load(read_file)
        draw()


def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        with open(filepath, "w") as write_file:
            json.dump(board, write_file)
    draw()


def key_press(event):
    global color
    color = int(event.char)



def click(event):
    row = event.y // w
    col = event.x // w
    x = event.x % w
    y = event.y % w
    if p < 0:
        board[row][col][0] = (board[row][col][0] + 1) % 2
        draw()
        return
    if board[row][col][0] == 0:
        if x >= y:
            t = 1
        else:
            t = 2
    else:
        if x + y < w:
            t = 1
        else:
            t = 2
    # print(row, col, t, board[row][col])
    u = board[row][col][t + 2]
    for i in range(n):
        for j in range(m):
            if board[i][j][3] == u:
                board[i][j][1] = color
            if board[i][j][4] == u:
                board[i][j][2] = color
    # print(colors[board[row][col][t]], board[row][col][t + 2])
    draw()
    # print(neightbour(row, col, board[row][col][0], t - 1))
    flag = True
    for i in range(n):
        for j in range(m):
            s = board[i][j][0]
            for k in range(2):
                self_c = board[i][j][k + 1]
                if self_c == 0:
                    flag = False
                self_a = board[i][j][k + 3]
                nb = neightbour(i, j, s, k)
                for ii, jj, kk in nb:
                    try:
                        other_c = board[ii][jj][kk + 1]
                        other_a = board[ii][jj][kk + 3]
                        if self_c == other_c and self_a != other_a:
                            flag = False
                    except:
                        print(len(board), len(board[0]))
                        print(nb, ii, jj, kk)
                        exit()
    print(flag)


def new_game():
    global board
    board = []
    for i in range(n):
        line = []
        for i in range(m):
            line.append([0, 0, 0, 0, 0])
        line.append([0, -1, -1, -1, -1])
        board.append(line)
    board.append([[0, -1, -1, -1, -1] for i in range(m + 1)])


color = 0
n = m = 15
w = 45
board = []
new_game()
colors = ["white", "yellow", "green", "blue", "red"]
p = 0
root = Tk()
mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Новый", command=new_game)
filemenu.add_command(label="Открыть...", command=open_file)
filemenu.add_command(label="Сохранить...", command = save_file)
filemenu.add_command(label="Выход")

mainmenu.add_cascade(label="Файл",
                     menu=filemenu)
# helpmenu = Menu(mainmenu, tearoff=0)
# helpmenu.add_command(label="Помощь")
# helpmenu.add_command(label="О программе")
# mainmenu.add_cascade(label="Справка",
#                      menu=helpmenu)
root.geometry(f"{n * w + 10}x{m * w + 10}")

canvas = Canvas(bg="white", width=n * w, height=m * w)
canvas.pack()
draw()
canvas.bind("<Button>", click)
root.bind("<KeyPress>", key_press)

root.mainloop()
