n = int(input("Сколько чисел вы хотите ввести? "))
max_value = float(input("Введите число 1: "))
i = 2
while i <= n:
    x = float(input("Введите число " + str(i) + ": "))
    if x > max_value:
        max_value = x
    i = i + 1
print("Максимальное число:", max_value)