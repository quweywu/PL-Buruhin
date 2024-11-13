from random import randint

def is_magic_square(matrix):
  n = len(matrix)
  
  for row in matrix:
    if len(row) != n:
      return False
  
  sum_row = sum(matrix[0])
  
  for i in range(1, n):
    if sum(matrix[i]) != sum_row:
      return False
  
  for j in range(n):
    sum_col = 0
    for i in range(n):
      sum_col += matrix[i][j]
    if sum_col != sum_row:
      return False
  
  sum_diag1 = 0
  sum_diag2 = 0
  for i in range(n):
    sum_diag1 += matrix[i][i]
    sum_diag2 += matrix[i][n-i-1]
  if sum_diag1 != sum_row or sum_diag2 != sum_row:
    return False
  
  return True

n, m = 3, 4  
a = [[randint(-50, 50) for _ in range(m)] for _ in range(n)]

print("Матрица:")
for row in a:
  print(row)

if is_magic_square(a):
  print("Матрица является магическим квадратом.")
else:
  print("Матрица не является магическим квадратом.")