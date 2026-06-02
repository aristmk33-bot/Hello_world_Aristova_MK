n = int(input("Введите число N: "))
sum_squares = 0
i = 1
while i <= n:
    sum_squares = sum_squares + i * i
    i = i + 1
print("Сумма квадратов первых", n, "чисел:", sum_squares)