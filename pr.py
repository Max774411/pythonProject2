import random
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

# board = [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
#          [(0, 0, 0), (1, 0, 1), (0, 0, 1), (0, 0, 0), (0, 0, 0)],
#          [(0, 0, 0), (0, 1, 0), (1, 1, 1), (0, 0, 0), (0, 0, 0)],
#         [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
#        [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],]
board = []
for i in range(5):
    line = []
    for j in range(5):
        line.append((random.randint(0,1),random.randint(0,4),random.randint(0,4)))
    board.append(line)


def click(event):
    row = event.y//80
    col = event.x//80
    print(row,col,board[row][col])






colors = ["white", "yellow", "green", "blue", "red"]

root = Tk()
root.geometry("500x500")

canvas = Canvas(bg="white", width=400, height=400)
canvas.pack()
draw()
canvas.bind("<Button>", click)
root.mainloop()
