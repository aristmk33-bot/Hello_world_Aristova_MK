n = int(input("Введите размер массива: "))
arr = []
i = 0
while i < n:
    element = float(input("arr[" + str(i) + "] = "))
    arr.append(element)
    i = i + 1
sum_arr = 0
i = 0
while i < n:
    sum_arr = sum_arr + arr[i]
    i = i + 1
average = sum_arr / n
print("Среднее арифметическое элементов массива:", average)