
---

### Dokumentace (DOCUMENTATION.md)


# Dokumentace k úkolu ---TASK MANAGER---

## Přehled

Tento program slouží jako jednoduchý správce úkolů, který umožňuje uživateli:
- Přidávat nové úkoly s názvem a popisem.
- Zobrazovat seznam všech úkolů ve formě přehledné tabulky.
- Odstraňovat úkoly podle čísla nebo názvu s následným přečíslováním.
- Ukládat seznam úkolů do textového souboru před ukončením programu.

## Popis funkcí

### hlavni_menu()
- **Účel:** Zobrazení hlavního menu s nadpisem a volbami.
- **Chování:** Vypíše nadpis, podtržení a nabídku možností (1. Přidat úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol, 4. Konec programu).

### pridat_ukol()
- **Účel:** Přidání nového úkolu.
- **Vstupy:** Uživatel zadá název a popis úkolu.
- **Zpracování:** Pokud alespoň jeden z údajů není prázdný, vytvoří se slovník s klíči `"Číslo"`, `"Název"` a `"Popis"` a úkol se přidá do seznamu `ukoly`.
- **Výstup:** Informace o přidaném úkolu se vypíše na obrazovku.

### zobrazit_ukoly()
- **Účel:** Zobrazení všech aktuálně přidaných úkolů.
- **Zpracování:** Pokud je seznam `ukoly` prázdný, vypíše se zpráva o neexistenci úkolů. Jinak se vypíše formátovaná tabulka obsahující číslo, název a popis každého úkolu.
- **Výstup:** Seznam úkolů ve formě tabulky.

### odstranit_ukol()
- **Účel:** Odstranění úkolu podle čísla nebo názvu.
- **Vstupy:** Uživatel zadá číslo nebo název úkolu, který chce odstranit.
- **Zpracování:** Prohledá se seznam úkolů a pokud se najde shoda, úkol se odstraní a následně se přečíslují zbývající úkoly.
- **Výstup:** Zpráva o úspěšném odstranění nebo upozornění, že úkol nebyl nalezen.

### ulozeni_ukolu()
- **Účel:** Uložení aktuálního seznamu úkolů do souboru.
- **Vstupy:** Globální proměnná `nazev_souboru` obsahující jméno souboru zadané uživatelem.
- **Zpracování:** Otevře se textový soubor v režimu zápisu a každý úkol se zapíše na jeden řádek ve formátované podobě.
- **Výstup:** Soubor s uloženým seznamem úkolů.

## Hlavní smyčka programu

- **Funkce:** Program běží ve smyčce, kde se opakovaně zobrazí hlavní menu a vyčká se na volbu uživatele.
- **Volby:**
  - **"1":** Spustí se funkce pro přidání úkolu.
  - **"2":** Spustí se funkce pro zobrazení úkolů.
  - **"3":** Spustí se funkce pro odstranění úkolu.
  - **"4":** Vyvolá se vnořený cyklus, který se zeptá, zda má uživatel uložit seznam úkolů před ukončením programu. Podle odpovědi se seznam uloží či ne a následně se hlavní smyčka ukončí.

## Závěr

Tato dokumentace popisuje strukturu a funkčnost programu Správce úkolů. Program je jednoduchý na údržbu a rozšíření, a je vhodný pro základní správu úkolů s možností uložení do textového souboru.
