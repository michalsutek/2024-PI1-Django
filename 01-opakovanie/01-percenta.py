max_bodov = 30
pocet_bodov = int(input("Zadaj počet bodov: "))
percenta = (pocet_bodov / max_bodov) * 100
print(f"Získal si {round(percenta, 2)}%") # round je funkcia na zaokruhlenie desat. cisla

if percenta >= 90:
    print("Výborný")
elif 75 <= percenta:
    print("Chválitebný")
elif 50 <= percenta:
    print("Dobrý")
elif 30 <= percenta:
    print("Dostatočný")
else:
    print("Nedostatočný!!!")
