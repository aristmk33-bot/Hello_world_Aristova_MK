n = int(input("Введите число N: "))
sum_n = 0
i = 1
while i <= n:
    sum_n = sum_n + i
    i = i + 1
print("Сумма первых", n, "натуральных чисел:", sum_n)