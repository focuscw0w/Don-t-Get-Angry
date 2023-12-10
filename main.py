import random

# Funkcia, ktorá v šachovnici zisťuje pozíciu hráča na základe riadka a stĺpca
def najdi_poziciu_hraca(sachovnica, hrac):
    suradnice = ["", ""]
    for i in range(len(sachovnica)):
        riadok = sachovnica[i]
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

    # Dopĺňanie symbolov do šachovnice, aby bol vytvorený kríž
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
    pozicia_pred_domcekom = [1, suradnica_pred_domcekom]
    
    # Cyklus bude prebiehať až dokedy nebude hráč v domčeku
    for i in range(999999):
        hod_kockou = random.randint(1, 6)
        pozicia_hraca = najdi_poziciu_hraca(sachovnica, "A")
    
        for i in range(hod_kockou):
            pozicia_hraca = najdi_poziciu_hraca(sachovnica, "A")
            
            # Ak je hráč v domčeku, hra sa zastaví
            if pozicia_hraca == pozicia_pred_domcekom and hod_kockou < (len(sachovnica) - 1) // 2:
                sachovnica[pozicia_hraca[0] + hod_kockou][pozicia_hraca[1] + 1] = "A"
                sachovnica[pozicia_pred_domcekom[0]][pozicia_pred_domcekom[1]] = "*"
                pozicia_hraca = najdi_poziciu_hraca(sachovnica, "A")
                print(f"Hráč hodil číslo {hod_kockou}")
                print(f"Hráč je v domčeku")
                return sachovnica

            sachovnica[pozicia_hraca[0]][pozicia_hraca[1]] = "*"
                
            # Ak je hráč za polovicou v osi X (na pravej strane)
            if sachovnica[pozicia_hraca[0]] != sachovnica[-1] and pozicia_hraca[1] > sirka_ramena + 1:
            # Kam má hráč zabočiť
                if sachovnica[pozicia_hraca[0] + 1][pozicia_hraca[1]] == "D":
                    sachovnica[pozicia_hraca[0]][pozicia_hraca[1] + 1] = "A" 

                elif sachovnica[pozicia_hraca[0] + 1][pozicia_hraca[1]] == "*":
                    sachovnica[pozicia_hraca[0] + 1][pozicia_hraca[1]] = "A"
                
                elif sachovnica[pozicia_hraca[0] - 1][pozicia_hraca[1]] == "*" and sachovnica[pozicia_hraca[0]][pozicia_hraca[1] - 1] == "*":
                    sachovnica[pozicia_hraca[0]][pozicia_hraca[1] - 1] = "A"

                elif sachovnica[pozicia_hraca[0] + 1][pozicia_hraca[1]] != "D":
                    sachovnica[pozicia_hraca[0]][pozicia_hraca[1] - 1] = "A"
                
                else:
                    sachovnica[pozicia_hraca[0]][pozicia_hraca[1] + 1] = "A"

            elif sachovnica[pozicia_hraca[0]][pozicia_hraca[1] - 1] == "*" and sachovnica[pozicia_hraca[0]] == sachovnica[-1]:
                sachovnica[pozicia_hraca[0]][pozicia_hraca[1] - 1] = "A"

            elif sachovnica[pozicia_hraca[0] - 1][pozicia_hraca[1]] == "*":
                sachovnica[pozicia_hraca[0] - 1][pozicia_hraca[1]] = "A"
            
            elif sachovnica[pozicia_hraca[0] - 1][pozicia_hraca[1]] == "D":
                sachovnica[pozicia_hraca[0]][pozicia_hraca[1] - 1] = "A"
            else:
                sachovnica[pozicia_hraca[0]][pozicia_hraca[1] + 1] = "A"

        print(f"Hráč hodil číslo {hod_kockou}")
        tlacsachovnicu(sachovnica)
        print("\n")

    return sachovnica

def tlacsachovnicu(sachovnica):
   for riadok in sachovnica:
        print(" ".join(riadok))

# Vstup
velkost_sachovnice = int(input("Zadajte veľkosť šachovnice: "))
dokoncena_sachovnica = gensachovnicu(velkost_sachovnice)
tlacsachovnicu(dokoncena_sachovnica)
