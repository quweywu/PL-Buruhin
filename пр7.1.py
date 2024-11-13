n = int(input("Введите размер массива: "))
array = [int(input()) for _ in range(n)]  
min_index = array.index(min(array))  
print("Индекс минимального элемента:", min_index)