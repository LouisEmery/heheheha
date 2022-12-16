import random

class Hero()
    def __init__(self):
        self.pdv = random.randint(1, 10) + random.randint(1, 10)
        self.force_attaque = random.randint(1, 6)
        self.force_defence = random.randint(1, 6)
        self.name = 'Louis'