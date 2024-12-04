# Чтение данных из файла
with open('Бурухин Никита Владимирович_У-243_vvod.txt', 'r') as fl:
    lines = fl.readlines()

# Создание матрицы из прочитанных строк
matrix = []
for line in lines:
    cl = line.replace('[', '').replace(']', '').replace(',', '').strip()
    if cl: 
        row = list(map(int, cl.split()))
        matrix.append(row)

def is_magic_square(matrix):
    n = len(matrix)
    
    # Проверка, что все строки имеют одинаковую длину
    for row in matrix:
        if len(row) != n:
            return False
    
    # Сумма первой строки
    sum_row = sum(matrix[0])
    
    # Проверка суммы строк
    for i in range(1, n):
        if sum(matrix[i]) != sum_row:
            return False
    
    # Проверка суммы столбцов
    for j in range(n):
        sum_col = sum(matrix[i][j] for i in range(n))
        if sum_col != sum_row:
            return False
    
    # Проверка суммы диагоналей
    sum_diag1 = sum(matrix[i][i] for i in range(n))
    sum_diag2 = sum(matrix[i][n-i-1] for i in range(n))
    
    if sum_diag1 != sum_row or sum_diag2 != sum_row:
        return False
    
    return True

print("Матрица:")
for row in matrix:
    print(row)

if is_magic_square(matrix):
    print("Матрица является магическим квадратом.")
else:
    print("Матрица не является магическим квадратом.")
    n = int(input("Введите размер матрицы (N): "))
    
    # Считывание новой матрицы от пользователя
    matrix = []
    print("Введите элементы матрицы:")
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    # Проверка на достаточную длину строк
    if all(len(row) >= 2 for row in matrix):  # Убедимся, что каждая строка имеет хотя бы 2 элемента
        # Обмен местами первого и последнего элемента в каждой строке
        for i in range(n):
            matrix[i][0], matrix[i][-1] = matrix[i][-1], matrix[i][0]
        
        print("Измененная матрица:")
        for row in matrix:
            print(row)
    else:
        print("Ошибка: все строки должны содержать как минимум 2 элемента.")

# Запись измененной матрицы в файл
with open('Бурухин Никита Владимирович_У-243_vivod.txt', 'w') as fl:
    for row in matrix:
        fl.write(' '.join(map(str, sorted(row))) + "\n")
