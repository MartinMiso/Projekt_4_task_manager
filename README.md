# Správce úkolů

Tento program je jednoduchý správce úkolů napsaný v Pythonu. Umožňuje uživateli:

- **Přidat úkol:** Zadáním názvu a popisu úkolu se úkol přidá do seznamu s automaticky přiřazeným pořadovým číslem.
- **Zobrazit úkoly:** Vypíše všechny aktuálně přidané úkoly v přehledné tabulce.
- **Odstranit úkol:** Umožňuje odstranit úkol na základě čísla nebo názvu. Po odstranění dojde k přečíslování zbývajících úkolů.
- **Ukončit program:** Při ukončení programu se uživatele zeptá, zda chce uložit seznam úkolů do souboru.

## Jak program spustit

1. Ujistěte se, že máte nainstalovaný Python 3.x.
2. Otevřete terminál nebo příkazový řádek.
3. Spusťte program pomocí:
   ```bash
   python main.py
Podle zobrazeného hlavního menu vyberte požadovanou možnost zadáním čísla (1-4).

Struktura programu
hlavni_menu()
Zobrazuje nadpis a možnosti hlavního menu.

pridat_ukol()
Umožňuje zadat název a popis úkolu. Úkol se uloží jako slovník do globálního seznamu ukoly s klíči "Číslo", "Název" a "Popis".

zobrazit_ukoly()
Vypíše všechny úkoly ve formě tabulky. Pokud nejsou žádné úkoly přidány, zobrazí se odpovídající zpráva.

odstranit_ukol()
Umožňuje odstranit úkol podle čísla nebo názvu. Při úspěšném odstranění dojde k přečíslování zbylých úkolů, aby pořadí odpovídalo jejich pozici v seznamu.

ulozeni_ukolu()
Ukládá seznam úkolů do textového souboru s názvem zadaným uživatelem. Každý úkol se uloží na jeden řádek s formátovanými sloupci.

Ukončení programu
Po výběru možnosti 4 se program zeptá, zda chcete uložit seznam úkolů do souboru:

Zadáním a (ano) se spustí funkce ulozeni_ukolu(), kde zadáte název souboru. Seznam se uloží a program se ukončí.

Zadáním n (ne) se program ukončí bez uložení seznamu úkolů.

Poznámky
V případě zadání prázdného názvu i popisu se úkol nepřidá a uživatel bude vyzván k opakovanému zadání.

Při odstraňování úkolu se nejprve ověří, zda zadaný úkol existuje. Pokud ne, zobrazí se chybová zpráva.

Program byl vyvinut s ohledem na jednoduchost a přehlednost, aby bylo snadné jej dále upravovat či rozšiřovat.
