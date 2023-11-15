# Časť prvá

def gensachovnicu(n):
    # Kotrola -> vstup nesmie byť párne číslo
    # Ak je vstup párne číslo - vráti to error a rovno upozorní používateľa ako má postupovať
    if n % 2 == 0:
        raise ValueError("Rozmer šachovnice musí byť nepárne číslo. Zadajte prosím číslo, ktoré nie je párne.")
    
    # Zadefinovanie šachovnice
    sachovnica = []

    # Vytvoríme prázdnu šachovnicu, ktorá bude reprezentovaná riadkami
    # Riadky sa budú plniť na základe určitej logiky v kóde nižšie
    for i in range(n):
        riadok_sachovnice = []
        for j in range(n):
            riadok_sachovnice.append(" ")
        sachovnica.append(riadok_sachovnice)

    # Podľa tejto logiky sa najskôr vypočíta šírka ramena
    # Na základe toho program zistí, že v akej pozícii bude "medzera" medzi ramenami
    sirka_ramena = (n - 3) // 2
    for i in range(sirka_ramena, sirka_ramena + 3):
        # Do šachovnice sa pridajú hviezdičky, ktoré hraničia s "borderom" šachovnice
        sachovnica[0][i] = "*"
        sachovnica[n - 1][i] = "*"
        sachovnica[i][0] = "*"
        sachovnica[i][n - 1] = "*"
    
    for i in range(1, n - 1):
        # Do šachovnice sa pridajú políčka pre domček
        sachovnica[i][sirka_ramena + 1] = "D"
        sachovnica[sirka_ramena + 1][i] = "D"

    # Do stredu šachovnice sa pridá bod "X"
    sachovnica[sirka_ramena + 1][sirka_ramena + 1] = "X"

    for i in range(sirka_ramena):
        # V tomto for cykle sa do šachovnice pridajú všetky jednotlivé symboly "*"

        # Postupuje sa najskôr podľa osi x
        # X
        sachovnica[sirka_ramena][i + 1] = "*"
        sachovnica[sirka_ramena][sirka_ramena + 2 + i] = "*"

        sachovnica[sirka_ramena + 2][i + 1] = "*"
        sachovnica[sirka_ramena + 2][sirka_ramena + 2 + i] = "*"

        # Potom podľa osi y
        # Y
        sachovnica[sirka_ramena - i][sirka_ramena] = "*"
        sachovnica[sirka_ramena - i][sirka_ramena + 2] = "*"

        sachovnica[sirka_ramena + 2 + i][sirka_ramena] = "*"
        sachovnica[sirka_ramena + 2 + i][sirka_ramena + 2] = "*"

    # Dokončenú šachovnicu "vrátime" z funkcie von pre ďalšie použitie    
    return sachovnica


def tlacsachovnicu(sachovnica):
    for riadok in sachovnica:
        print(riadok)

dokoncena_sachovnica = gensachovnicu(9)
tlacsachovnicu(dokoncena_sachovnica)

# Časť druhá

def simulacia_pohybu(sachovnica):
    pass