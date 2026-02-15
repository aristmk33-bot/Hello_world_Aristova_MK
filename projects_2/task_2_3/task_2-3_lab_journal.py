# Программа для электронного лабораторного журнала

# Собираем данные
researcher_name = input("Введите ФИО исследователя: ")
date = input("Введите дату (ДД.ММ.ГГГГ): ")
experiment_name = input("Введите название эксперимента: ")
conclusion = input("Введите вывод: ")

# Записываем данные в файл с рамкой
with open("journal.txt", "w", encoding="utf-8") as file:
    file.write("+---+---+\n")
    file.write("| Электронный лабораторный журнал    |\n")
    file.write("+---+---+\n")
    file.write(f"| ФИО исследователя : {researcher_name}    |\n")
    file.write(f"| Дата    : {date}    |\n")
    file.write(f"| Эксперимент    : {experiment_name}    |\n")
    file.write("+---+---+\n")
    file.write("| Вывод:    |\n")
    file.write(f"| {conclusion}    |\n")
    file.write("+---+---+\n")

print("Данные успешно сохранены в journal.txt")