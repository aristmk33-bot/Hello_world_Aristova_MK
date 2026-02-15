f = open("output.txt", "w", encoding="utf-8")

print("Имя: Мария", file=f)
print("Группа: 4731901/50001", file=f)
print("Возраст: 18 лет", file=f)
print("Любимый предмет: Информатика", file=f)

f.close()


print("Файл output.txt создан!")
