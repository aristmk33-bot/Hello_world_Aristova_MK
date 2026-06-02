n = int(input("Введите число N: "))
factorial = 1
i = 1
while i <= n:
    factorial = factorial * i
    i = i + 1
print("Факториал числа", n, "равен", factorial)