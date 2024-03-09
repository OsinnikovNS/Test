# Заполнение матрицы по спирали

def fun():

    n, m = map(int, input('Введите два натуральных числа через пробел: ').split())
    matrix = [[0] * m for _ in range(n)]
    dx, dy, x, y = 0, 1, 0, 0

    for i in range(1, n * m + 1):
        matrix[x][y] = i
        if matrix[(x + dx) % n][(y + dy) % m]:
            dx, dy = dy, -dx
        x += dx
        y += dy
    for line in matrix:
        print(*(f'{i:<3}' for i in line), sep='')
