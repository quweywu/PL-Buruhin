def modulo(a, b):
    if a < b:
        return a
    return modulo(a - b, b)
a = 10
b = 3
result = modulo(a, b)
print(f"Остаток от деления {a} на {b} равен {result}")