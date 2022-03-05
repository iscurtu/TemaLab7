"""
In prima faza, trebuie sa adaugam marca si numarul de inmatriculare al vehiculului. Dupa ce am adaugat aceste obiecte,
avem posibilitatea sa adaugam si prorpietatile la vehiculele pe care le-am adaugat initial. Putem afisa media kilometrilor
parcursi al tututror masinilor pe care le am adaugat.

"""

from Vehicul import Vehicul
from Masina import Masina
import sys

if __name__=="__main__":

    dict = {1: Masina.afisare_vehicule,
            2: Vehicul.adaugare,
            3: Masina.adaugare_autovehicul,
            4: Masina.afisare_medie_km,
            5: sys.exit
            }

    while True:
        optiune =input(""" 
    Alegeti optiunea dorita:
        1. Afisare nr. vehicule in garaj si marca acestora.
        2. Inregistrare model vehicul si numarul de inmatriculare
        3. Adaugare propietati autovehiculelor inregistrate.
        4. Afisarea mediei kilometrii parcursi.
        5. Iesire
        """)
        try:
            optiune = int(optiune)
        except ValueError:
            print("Nu ati introdus o cifra de tip int.")

        else:
           if optiune in dict:
              dict[optiune]()