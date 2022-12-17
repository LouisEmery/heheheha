import random
est_vivant = true

#DOMAGE A DEFINIR
domage = 5
class Hero()
    def __init__(self):
        self.pdv = random.randint(1, 10) + random.randint(1, 10)
        self.force_attaque = random.randint(1, 6)
        self.force_defence = random.randint(1, 6)
        self.name = 'Louis'
    def attack(self):
        return random.randint(1, 6) + self.force_attaque
    def degats_recu(self):
        return self.pdv -= domage - self.force_defence
    def est_vivant(self):
        if self.pdv <= 0
            return est_vivant = false
