volume = float(input("Введите нужный объем раствора (мл): "))

salt_mass = volume * 0.009

water_volume = volume

print("\n--- РЕЦЕПТ ПРИГОТОВЛЕНИЯ ---")
print(f"Общий объем: {volume} мл")
print(f"Масса соли: {salt_mass:.2f} г")
print(f"Объем воды: {water_volume} мл")

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("---\n")
    file.write(f"Общий объем: {volume} мл\n")
    file.write(f"Масса соли: {salt_mass:.2f} г\n")
    file.write(f"Объем воды: {water_volume} мл\n")

print("\nРецепт сохранен в файл recipe.txt")