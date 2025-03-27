def hlavni_menu():
    print("Správce úkolů - Hlavní menu")
    print("1. Přidat úkol", "\n2. Zobrazit všechny úkoly", "\n3. Odstranit úkol", "\n4. Konec programu")


def pridat_ukol():
    print("Přidám pak úkol")
    ukol = (input("Zadej název nebo popis úkolu: "))
    while True:
        if ukol != "":
            ukoly.append(ukol)
            print(f"Úkol {ukol} byl přidán.")
            continue
        else:
            print("Nezadal jsi název ani popis úkolu")



def zobrazit_ukoly():
    return print("Ukážu ti úkoly a pak něco dál")

def odstranit_ukol():
    return print("Voe smažem úkoly")

# Press the green button in the gutter to run the script.
ukoly = []
if __name__ == '__main__':

    while True:
        hlavni_menu()
        moznost = int(input("Vyberte možnost (1-4): "))
        print()
        if moznost == 1:
            pridat_ukol()
            print()
        elif moznost == 2:
            zobrazit_ukoly()
            print()
        elif moznost == 3:
            odstranit_ukol()
            print()
        elif moznost == 4:
            print("Ukončuji program")
            break
        elif moznost == 5:
            print("Vypisuji úkoly")
            print(ukoly)
        else:
            print("Nezadal jsi správnou hodnotu, zadej správnou volbu.")

