from math import pi

class Cercle:
    def init(self, rayon):
        self.rayon = rayon

    def calcul_aire(self):
        return pi * self.rayon*2

    def calcul_circonference(self):
        return 2pi*self.rayon
