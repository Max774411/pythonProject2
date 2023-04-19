def flood(a, i, j):
    a[i][j] = 2
    if a[i + 1][j] == 0:
        flood(a, i + 1, j)
    if a[i -1][j ] == 0:
        flood(a, i -1, j)
    if a[i][j + 1] == 0:
        flood(a, i, j + 1)
    if a[i][j-1] ==0:
        flood(a, i, j-1)


board = [[0, 1, 1, 1, 1],
         [0, 1, 0, 0, 1],
         [0, 1, 0, 0, 1],
         [0, 1, 0, 0, 1],
         [0, 1, 1, 1, 1]]
for i in board:
    print(*i)
print()
flood(board, 2, 3)
for i in board:
    print(*i)
