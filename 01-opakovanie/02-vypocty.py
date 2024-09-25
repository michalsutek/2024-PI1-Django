def sucet(x, y):
    return x + y

def sucin(x, y):
    return x * y

def parne(cislo):
    if cislo % 2 == 0:
        return "párne"
    else:
        return "nepárne"


a = int(input("Zadaj a: "))
b = int(input("Zadaj b: "))

print(f"Súčet čísel {a} + {b} = {sucet(a, b)}")
print(f"Súčin čísel {a} + {b} = {sucin(a, b)}")

print(f"Číslo {a} je {parne(a)}")
print(f"Číslo {b} je {parne(b)}")

