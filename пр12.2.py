def second_largest():
    largest = second = 0
    while True:
        num = int(input("Введите натуральное число (0 для завершения): "))
        if num == 0:
            break
        if num > largest:
            second = largest
            largest = num  
        elif num > second and num != largest:
            second = num 
    if second == 0:
        print("В последовательности недостаточно уникальных чисел для определения второго по величине.")
    else:
        print(f"Второй по величине элемент: {second}")
second_largest()