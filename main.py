def hlavni_menu():
    nadpis = "Správce úkolů - Hlavní menu"
    print(nadpis)
    podtrzeni = (len(nadpis) * "-")
    print(podtrzeni)
    print("1. Přidat úkol", "\n2. Zobrazit všechny úkoly", "\n3. Odstranit úkol", "\n4. Konec programu")


def pridat_ukol():
    print("Přidání úkolu:")
    while True:
        ukol_nazev = (input("Zadej název úkolu: "))
        ukol_popis = (input("Zadej popis úkolu: "))

        if ukol_nazev or ukol_popis != "":
            ukoly.append(ukol_nazev)
            ukoly.append((ukol_popis))
            print(f"Úkol '{ukol_nazev}' byl přidán.")
            break
        else:
            print("Nezadal jsi název ani popis úkolu.")



def zobrazit_ukoly():
    return print(f"Vypisuji úkoly \n{ukoly}")

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
        else:
            print("Nezadal jsi správnou hodnotu, zadej správnou volbu.")

