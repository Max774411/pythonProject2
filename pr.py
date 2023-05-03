from tkinter import Tk, Canvas


def draw():
    for i in range(5):
        for j in range(5):
            color1 = colors[board[i][j][1]]
            color2 = colors[board[i][j][2]]
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
            if shape == 1:
                canvas.create_polygon(j * 80, (i + 1) * 80, (j + 1) * 80, i * 80, j * 80, i * 80, fill=color1,
                                      outline=color1)
                canvas.create_polygon((j + 1) * 80, i * 80, (j + 1) * 80, (i + 1) * 80, j * 80, (i + 1) * 80,
                                      fill=color2, outline=color2)
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


board = [[(1, 1, 1, 1, 1), (1, 1, 1, 1, 1), (0, 0, 0, 0, 0), (0, 4, 4, 4, 4), (0, 4, 4, 4, 4), (0, -1, -1, -1, -1)],
         [(0, 0, 0, 0, 0), (0, 1, 0, 1, 0), (0, 0, 0, 0, 0), (1, 4, 0, 4, 0), (0, 0, 0, 0, 0), (0, -1, -1, -1, -1)],
         [(0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, -1, -1, -1, -1)],
         [(0, 0, 0, 0, 0), (1, 0, 2, 0, 2), (0, 0, 0, 0, 0), (0, 0, 3, 0, 3), (0, 0, 0, 0, 0), (0, -1, -1, -1, -1)],
         [(0, 2, 2, 2, 2), (0, 2, 2, 2, 2), (0, 0, 0, 0, 0), (1, 3, 3, 3, 5), (0, 3, 3, 5, 5), (0, -1, -1, -1, -1)],
         [(0, -1, -1, -1, -1), (0, -1, -1, -1, -1), (0, -1, -1, -1, -1), (0, -1, -1, -1, -1), (0, -1, -1, -1, -1),
          (0, -1, -1, -1, -1)]]


# board = []
# for i in range(5):
#     line = []
#     for j in range(5):
#         line.append((random.randint(0,1),random.randint(0,4),random.randint(0,4)))
#     board.append(line)


def click(event):
    row = event.y // 80
    col = event.x // 80
    x = event.x % 80
    y = event.y % 80
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
    print(colors[board[row][col][t]], board[row][col][t + 2])


colors = ["white", "yellow", "green", "blue", "red"]

root = Tk()
root.geometry("500x500")

canvas = Canvas(bg="white", width=400, height=400)
canvas.pack()
draw()
canvas.bind("<Button>", click)
root.mainloop()
