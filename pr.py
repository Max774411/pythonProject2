from tkinter import Tk, Canvas


def draw():
    for i in range(5):
        for j in range(5):
            color = colors[board[i][j] % 5]
            shape = board[i][j] // 5
            if shape == 0:
                print(color)
                canvas.create_rectangle(j * 80, i * 80, (j + 1) * 80, (i + 1) * 80, fill=color)
            if shape == 1:
                canvas.create_polygon(j*80, i*80,(j+1)*80, (i+1)*80, (j+1)*80,i*80, fill=color, outline='black')


board = [[0, 1, 2, 3, 4],
         [5, 6, 7, 8, 9],
         [10, 11, 12, 13, 14],
         [25, 16, 17, 18, 19],
         [20, 21, 22, 23, 24]]

colors = ["white", "black", "green", "blue", "red"]

root = Tk()
root.geometry("500x500")

canvas = Canvas(bg="white", width=400, height=400)
canvas.pack()
draw()
# canvas.create_polygon(22, 33, 50, 55, 33, 100, fill = 'orange', outline ='black')
root.mainloop()
