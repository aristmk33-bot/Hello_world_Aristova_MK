a = float(input("Введите число 1: "))
b = float(input("Введите число 2: "))
c = float(input("Введите число 3: "))
d = float(input("Введите число 4: "))
min_value = a
if b < min_value:
    min_value = b
if c < min_value:
    min_value = c
if d < min_value:
    min_value = d
print("Минимальное число:", min_value)