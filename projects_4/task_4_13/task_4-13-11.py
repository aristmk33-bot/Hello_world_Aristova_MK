n = int(input("Введите размер массива: "))
arr = []
i = 0
while i < n:
    element = float(input("arr[" + str(i) + "] = "))
    arr.append(element)
    i = i + 1
sum_even_index = 0
count_even_index = 0
i = 0
while i < n:
    if i % 2 == 0:
        sum_even_index = sum_even_index + arr[i]
        count_even_index = count_even_index + 1
    i = i + 1
average = sum_even_index / count_even_index
print("Среднее арифметическое элементов с чётными индексами:", average)