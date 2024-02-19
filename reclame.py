from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    smaak = "aardbei"
    nieuwe_prijs = prijs * (1 - korting)
    nieuwe_prijs = round(nieuwe_prijs, 2)
    boodschap = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."
    return boodschap


def inkomsten_totaal(inkomsten, btw=0):
    totaal = sum(inkomsten)
    bedrag = totaal * btw
    bedrag = round(bedrag, 2)
    informatie = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    return informatie


def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    resultaat = [hoogste, laagste]
    return resultaat


def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    gemiddelde = totaal / len(mijn_lijst)
    gemiddelde = round(gemiddelde, 2)
    informatie = f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
    return informatie


def meervoudig(invoer_lijst):
    resultaat = laag_en_hoog(invoer_lijst)
    return resultaat

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer