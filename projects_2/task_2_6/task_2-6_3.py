donor = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Введите группу крови пациента (I, II, III, IV): ").strip().upper()

if donor == recipient or donor == "I":
    print("Кровь можно перелить")
else:
    print("Кровь нельзя перелить")