
class Vehicul:

    lista_vehicule = []

    def __init__(self, marca_vehicul, numar_inmatriculare):

        self.numar_inmatriculare = numar_inmatriculare
        self.__marca_vehicul = marca_vehicul

    def afisare_marca(self):
        return self.__marca_vehicul

    def nr_matricol(self):
        return self.numar_inmatriculare


    @classmethod
    def adaugare(cls):
        numar_inmatriculare = input("Numar inmatriculare: ")
        count = 0
        for i in cls.lista_vehicule:
            if i.nr_matricol() == numar_inmatriculare:
                count += 1

        if count == 0:
            marca_vehicul = input("Marca vehicul: ")
            obiect = Vehicul(marca_vehicul, numar_inmatriculare)
            Vehicul.lista_vehicule.append(obiect)

            return None
        print("Un vehicul cu acest numar de inmatriculare deja se afla in garaj.")






