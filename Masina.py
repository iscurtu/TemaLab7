from Vehicul import Vehicul

class Masina(Vehicul):
    lista_masini = []
    count = 0
    suma = 0
    def __init__(self, marca_vehicul, numar_inmatriculare,  dimensiune_motor, viteza_maxima, kilometraj, an_fabricare):
        Vehicul.__init__(self, marca_vehicul, numar_inmatriculare)

        self.dimensiune_motor = dimensiune_motor
        self.viteza_maxima = viteza_maxima
        self.kilometraj = kilometraj
        self.an_fabricare = an_fabricare
        Masina.count += 1
        Masina.suma += self.kilometraj

    @classmethod
    def adaugare_autovehicul(cls):
        optiune = input("Nr. inmatriculare pentru a vedea daca masina a fost inregistrata. ")
        for i in cls.lista_vehicule:
            if i.nr_matricol() == optiune:
                dimensiune_motor = input("Dimensiune motor: ")
                viteza_maxima = input("Viteza maxima: ")
                kilometraj = int(input("Kilometrajul: "))
                an_fabricare = input("Anul fabricarii: ")
                obiect = Masina(i.afisare_marca(), i.nr_matricol(), dimensiune_motor, viteza_maxima, kilometraj, an_fabricare)
                Masina.lista_masini.append(obiect)


                return None

        print("Vehiculul cu numarul respectiv de inmatriculare nu se afla in garaj.")


    @classmethod
    def afisare_medie_km(cls):

       try:
          Masina.suma / Masina.count
       except ZeroDivisionError:
          print("Impartirea la 0 nu este posibila.")
       else:
          print("Media kilometrilor parcursi de masinile din garaj este:", Masina.suma / Masina.count)

    @classmethod
    def afisare_vehicule(cls):
         if len(cls.lista_masini) == 0:
            print("Chiar daca avem modele inregistrate, nu cunoastem restul detaliilor, iar informatia nu poate fi furnizata")

         else:
            for i in cls.lista_masini:
                print(i.afisare_marca(), i.nr_matricol(), i.dimensiune_motor, i.viteza_maxima, i.kilometraj, i.an_fabricare)
                print("##################################")

