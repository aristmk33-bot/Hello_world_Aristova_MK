total_capsules = int(input("Введите общее количество произведенных капсул: "))
pack_capacity = int(input("Введите вместимость одной упаковки (шт): "))

full_packs = total_capsules // pack_capacity
remaining_capsules = total_capsules % pack_capacity

print(f"\nРезультат фасовки:")
print(f"Полных упаковок: {full_packs}")
print(f"Остаток капсул: {remaining_capsules}")