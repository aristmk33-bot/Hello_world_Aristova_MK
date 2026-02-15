print("=== Анализ последовательности ДНК ===\n")

dna_sequence = input("Введите последовательность ДНК: ")

dna_upper = dna_sequence.upper()

print(f"\nПоследовательность в верхнем регистре: {dna_upper}")

count_A = dna_upper.count('A')
count_T = dna_upper.count('T')
count_G = dna_upper.count('G')
count_C = dna_upper.count('C')

total_length = len(dna_upper)

print("\nПодсчёт нуклеотидов:")
print(f"A: {count_A}")
print(f"T: {count_T}")
print(f"G: {count_G}")
print(f"C: {count_C}")

print(f"\nОбщая длина: {total_length} нуклеотидов")

if total_length > 0:
    print("\nПроцентное содержание:")
    print(f"A: {(count_A / total_length * 100):.1f}%")
    print(f"T: {(count_T / total_length * 100):.1f}%")
    print(f"G: {(count_G / total_length * 100):.1f}%")
    print(f"C: {(count_C / total_length * 100):.1f}%")