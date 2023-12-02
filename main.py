import random

def najdi_poziciu_hraca(sachovnica, hrac):
    suradnice = ["", ""]
    for i, riadok in enumerate(sachovnica):
        if hrac in riadok:
            suradnice[0] = i
            suradnice[1] = riadok.index(hrac)
    return suradnice

def gensachovnicu(n):
    # Kotrola -> vstup nesmie byť párne číslo
    if n % 2 == 0:
        raise ValueError("Rozmer šachovnice musí byť nepárne číslo. Zadajte prosím číslo, ktoré nie je párne.")
    
    sachovnica = []

    for i in range(n):
        riadok_sachovnice = []
        for j in range(n):
            riadok_sachovnice.append(" ")
        sachovnica.append(riadok_sachovnice)

    sirka_ramena = (n - 3) // 2

    for i in range(sirka_ramena, sirka_ramena + 3):
        sachovnica[0][i] = "*"
        sachovnica[n - 1][i] = "*"
        sachovnica[i][0] = "*"
        sachovnica[i][n - 1] = "*"
    
    for i in range(1, n - 1):
        sachovnica[i][sirka_ramena + 1] = "D"
        sachovnica[sirka_ramena + 1][i] = "D"

    sachovnica[sirka_ramena + 1][sirka_ramena + 1] = "X"

    for i in range(sirka_ramena):
        # X
        sachovnica[sirka_ramena][i + 1] = "*"
        sachovnica[sirka_ramena][sirka_ramena + 2 + i] = "*"

        sachovnica[sirka_ramena + 2][i + 1] = "*"
        sachovnica[sirka_ramena + 2][sirka_ramena + 2 + i] = "*"

        # Y
        sachovnica[sirka_ramena - i][sirka_ramena] = "*"
        sachovnica[sirka_ramena - i][sirka_ramena + 2] = "*"

        sachovnica[sirka_ramena + 2 + i][sirka_ramena] = "*"
        sachovnica[sirka_ramena + 2 + i][sirka_ramena + 2] = "*"

    # Číslovanie riadkov
    for i, riadok in enumerate(sachovnica):
        riadok.insert(0, f"{i % 10 :2d}")
    
    # Číslovanie stĺpcov
    stlpce = []
    for i in range(n):
        stlpce.append(f"{i % 10:2d}".replace(" ", ""))
    stlpce.insert(0, "  ")
    sachovnica.insert(0, stlpce)

    # Nastavenie pozície hráča
    sachovnica[1][sirka_ramena + 3] = "A"
    suradnica_pred_domcekom = sachovnica[1].index(sachovnica[1][sirka_ramena + 2])
    pozicia_pred_domcekom = sachovnica[1][suradnica_pred_domcekom]

    # Simulácia pohybu - TODO: Spraviť funkciu
    hod_kockou = random.randint(1, 6)
    hod_kockou = 8
    print(f"Hráč hodil číslo {hod_kockou}")
    print("\n")
    
    for i in range(hod_kockou):
        pozicia_hraca = najdi_poziciu_hraca(sachovnica, "A")
        sachovnica[pozicia_hraca[0]][pozicia_hraca[1]] = "*"

        # Kam má hráč zabočiť
        if sachovnica[pozicia_hraca[0] + 1][pozicia_hraca[1]] == "D" and sachovnica[pozicia_hraca[0]][pozicia_hraca[1] + 1] == "*":
            sachovnica[pozicia_hraca[0]][pozicia_hraca[1] + 1] = "A" 
        
        elif sachovnica[pozicia_hraca[0] + 1][pozicia_hraca[1]] == "*":
            sachovnica[pozicia_hraca[0] + 1][pozicia_hraca[1]] = "A"
       
        # TODO: Ak je nad hráčom domček, ide doľava

    return sachovnica


def tlacsachovnicu(sachovnica):
   for riadok in sachovnica:
        print(" ".join(riadok))

velkost_sachovnice = int(input("Zadajte veľkosť šachovnice: "))
dokoncena_sachovnica = gensachovnicu(velkost_sachovnice)
tlacsachovnicu(dokoncena_sachovnica)

    