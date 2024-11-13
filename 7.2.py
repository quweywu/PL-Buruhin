n = int(input("Введите размер массива: "))
array = [int(input()) for _ in range(n)]

positive_array = [x for x in array if x > 0]
negative_array = [x for x in array if x <= 0]

print("Положительные элементы:", positive_array)
print("Остальные элементы:", negative_array)