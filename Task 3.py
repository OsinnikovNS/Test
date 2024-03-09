n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
if all(i in sum(matrix,[]) for i in range(1, n**2 + 1)):
    print('YES' if all(sum(i) == sum(j) == sum([matrix[i][i] for i in range(n)]) == sum([matrix[n-i-1][i] for i in range(n)]) for i in matrix for j in list(map(list, zip(*matrix)))) else 'NO')
else:
    print('NO')
# Пример ввода
#   3
#   8 1 6
#   3 5 7
#   4 9 2