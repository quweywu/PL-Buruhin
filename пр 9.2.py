n = int(input("Введите размер матрицы (N): "))
matrix = []
print("Введите элементы матрицы:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(n):
    matrix[i][0], matrix[i][n-1] = matrix[i][n-1], matrix[i][0]
print("Измененная матрица:")
for row in matrix:
    print(row)