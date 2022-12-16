

class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur

    def calcul_air(self):
        return self.largeur * self.longueur

    def afficher_info(self):
        print(self.calcul_air())

a = Rectangle(15, 10)
a.afficher_info()