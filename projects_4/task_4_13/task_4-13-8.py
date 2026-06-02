n = int(input("Введите размер массива: "))
arr = []
i = 0
while i < n:
    element = float(input("arr[" + str(i) + "] = "))
    arr.append(element)
    i = i + 1
positive_count = 0
i = 0
while i < n:
    if arr[i] > 0:
        positive_count = positive_count + 1
    i = i + 1
print("Количество положительных чисел:", positive_count)