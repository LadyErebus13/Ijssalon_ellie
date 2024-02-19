def mijn_functie_1(argument):
    tabel = {
        2:4, 
        4:16, 
        10:100, 
        12:144
        }
    return tabel.get(argument, "Ongeldige invoer")

print(mijn_functie_1())


def mijn_functie_2(argument):
    afgerond = round(argument)
    teruggeefwaarde = []
    teruggeefwaarde.append(afgerond + 3)
    teruggeefwaarde.append(afgerond - 3)
    teruggeefwaarde.append(afgerond * 3)
    teruggeefwaarde.append(round(afgerond / 3))
    return teruggeefwaarde

print(mijn_functie_2())