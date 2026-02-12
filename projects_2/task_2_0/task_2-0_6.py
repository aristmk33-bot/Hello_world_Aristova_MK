# открываем файл для записи
f = open("output.txt", "w", encoding="utf-8")

# пишем информацию о себе
print("Имя: Мария", file=f)
print("Группа: 4731901/50001", file=f)
print("Возраст: 18 лет", file=f)
print("Любимый предмет: Информатика", file=f)

# закрываем файл — обязательно!
f.close()

print("Файл output.txt создан!")