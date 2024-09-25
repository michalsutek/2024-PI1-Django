max_bodov = 30

# funkcia na získanie validného počtu bodov
def ziskaj_pocet_bodov():
    while True: # nekonečný cyklus
        try:
            pocet_bodov = int(input(f"Zadaj počet bodov (0 - {max_bodov}): "))
            if 0 <= pocet_bodov <= max_bodov:
                return pocet_bodov
            else:
                print(f"Počet bodov musí byť v rozsahu 0 po {max_bodov}. Daj ešte raz!")
        except ValueError:
            print("Neplatný vstup! Zadaj celé číslo")


def vypocitaj_percenta(pocet_bodov):
    return round((pocet_bodov / max_bodov) * 100, 2)


def klasifikacia(percenta):
    if percenta >= 90:
        return "Výborný"
    elif percenta >= 75:
        return "Chválitebný"
    elif percenta >= 50:
        return "Dobrý"
    elif percenta >= 30:
        return "Dostatočný"
    else:
        return "Nedostatočný!!!"


pocet_bodov = ziskaj_pocet_bodov()
percenta = vypocitaj_percenta(pocet_bodov)
hodnotenie = klasifikacia(percenta)
print(f"Počet bodov: {pocet_bodov}, Percentá: {percenta}%, Hodnotenie: {hodnotenie}")
