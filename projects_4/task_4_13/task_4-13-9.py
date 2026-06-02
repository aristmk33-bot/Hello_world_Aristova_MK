n = int(input("Введите размер массива: "))
arr = []
i = 0
while i < n:
    element = float(input("arr[" + str(i) + "] = "))
    arr.append(element)
    i = i + 1
sum_odd = 0
i = 0
while i < n:
    if arr[i] % 2 != 0:
        sum_odd = sum_odd + arr[i]
    i = i + 1
print("Сумма нечётных элементов:", sum_odd)