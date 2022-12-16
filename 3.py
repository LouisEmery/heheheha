from math import pi

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calcul_aire(self):
        return pi * self.rayon**2

    def afficher_info(self):
        print(self.calcul_aire())
        print(self.calcul_circonference())

    def calcul_circonference(self):
        return 2*pi*self.rayon

a = Cercle(5)
a.afficher_info()
