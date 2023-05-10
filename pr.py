from tkinter import Tk, Canvas, Menu, filedialog
import json


def draw():
    fnt = ('Helvetica 15 bold')

    for i in range(5):
        for j in range(5):
            color1 = colors[board[i][j][1]]
            color2 = colors[board[i][j][2]]
            ar1 = board[i][j][3]
            ar2 = board[i][j][4]
            shape = board[i][j][0]
            # if shape == 0:
            #     canvas.create_rectangle(j * 80, i * 80, (j + 1) * 80, (i + 1) * 80, fill=color1)
            # if shape == 1:
            #     canvas.create_polygon(j * 80, i * 80, (j + 1) * 80, (i + 1) * 80, (j + 1) * 80, i * 80, fill=color1,
            #                           outline='black')
            # if shape == 2:
            #     canvas.create_polygon(j * 80, (i + 1) * 80, (j + 1) * 80, (i + 1) * 80, j * 80, i * 80, fill=color1,
            #                           outline='black')
            # if shape == 3:
            #     canvas.create_polygon(j * 80, (i + 1) * 80, (j + 1) * 80, i * 80, j * 80, i * 80, fill=color1,
            #                           outline='black')
            #
            # if shape == 4:
            #     canvas.create_polygon((j + 1) * 80, i * 80, (j + 1) * 80, (i + 1) * 80, j * 80, (i + 1) * 80,
            #                           fill=color1, outline='black')

            if shape == 0:
                canvas.create_polygon(j * 80, i * 80, (j + 1) * 80, (i + 1) * 80, (j + 1) * 80, i * 80, fill=color1,
                                      outline=color1)

                canvas.create_polygon(j * 80, (i + 1) * 80, (j + 1) * 80, (i + 1) * 80, j * 80, i * 80, fill=color2,
                                      outline=color2)
                canvas.create_text(j * 80 + 60, i * 80 + 30, text=str(ar1), fill="black", font=fnt)
                canvas.create_text(j * 80 + 30, i * 80 + 60, text=str(ar2), fill="black", font=fnt)
            if shape == 1:
                canvas.create_polygon(j * 80, (i + 1) * 80, (j + 1) * 80, i * 80, j * 80, i * 80, fill=color1,
                                      outline=color1)
                canvas.create_polygon((j + 1) * 80, i * 80, (j + 1) * 80, (i + 1) * 80, j * 80, (i + 1) * 80,
                                      fill=color2, outline=color2)
                canvas.create_text(j * 80 + 30, i * 80 + 30, text=str(ar1), fill="black", font=fnt)
                canvas.create_text(j * 80 + 60, i * 80 + 60, text=str(ar2), fill="black", font=fnt)
            if board[i][j][3] != board[i][j][4]:  # диагональ
                if shape == 0:
                    canvas.create_line((j + 1) * 80, (i + 1) * 80, j * 80, i * 80, fill='black', width=3)
                if shape == 1:
                    canvas.create_line(j * 80, (i + 1) * 80, (j + 1) * 80, i * 80, fill='black', width=3)
            # левая сторона
            if board[i][j][4 - shape] != board[i][j - 1][3 + board[i][j - 1][0]]:
                canvas.create_line(j * 80, i * 80, j * 80, (i + 1) * 80, fill='black', width=3)
            # верхняя сторона
            if board[i][j][3] != board[i - 1][j][4]:
                canvas.create_line(j * 80, i * 80, (j + 1) * 80, i * 80, fill='black', width=3)


# board = [[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 4, 4, 4, 4], [0, 4, 4, 4, 4], [0, -1, -1, -1, -1]],
#          [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [1, 4, 0, 4, 0], [0, 0, 0, 0, 0], [0, -1, -1, -1, -1]],
#          [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, -1, -1, -1, -1]],
#          [[0, 0, 0, 0, 0], [1, 0, 2, 0, 2], [0, 0, 0, 0, 0], [0, 0, 3, 0, 3], [0, 0, 0, 0, 0], [0, -1, -1, -1, -1]],
#          [[0, 2, 2, 2, 2], [0, 2, 2, 2, 2], [0, 0, 0, 0, 0], [1, 3, 3, 3, 5], [0, 3, 3, 5, 5], [0, -1, -1, -1, -1]],
#          [[0, -1, -1, -1, -1], [0, -1, -1, -1, -1], [0, -1, -1, -1, -1], [0, -1, -1, -1, -1], [0, -1, -1, -1, -1],
#           [0, -1, -1, -1, -1]]]

board = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, -1, -1, -1, -1]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, -1, -1, -1, -1]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, -1, -1, -1, -1]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, -1, -1, -1, -1]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, -1, -1, -1, -1]],
         [[0, -1, -1, -1, -1], [0, -1, -1, -1, -1], [0, -1, -1, -1, -1], [0, -1, -1, -1, -1], [0, -1, -1, -1, -1],
          [0, -1, -1, -1, -1]]]


# board = []
# for i in range(5):
#     line = []
#     for j in range(5):
#         line.append((random.randint(0,1),random.randint(0,4),random.randint(0,4)))
#     board.append(line)


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
    global p

    if event.char == " ":
        p = -1
    elif event.char > "9":
        p = ord(event.char) - ord("a") + 10
    else:
        p = int(event.char)


def click(event):
    row = event.y // 80
    col = event.x // 80
    x = event.x % 80
    y = event.y % 80
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
        if x + y < 80:
            t = 1
        else:
            t = 2
    # print(row, col, t, board[row][col])
    board[row][col][t + 2] = p
    print(colors[board[row][col][t]], board[row][col][t + 2])
    draw()


colors = ["white", "yellow", "green", "blue", "red"]
p = 0
root = Tk()
mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Новый")
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
root.geometry("500x500")

canvas = Canvas(bg="white", width=400, height=400)
canvas.pack()
draw()
canvas.bind("<Button>", click)
root.bind("<KeyPress>", key_press)

root.mainloop()
