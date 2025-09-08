import random
from enemy import Enemy

class Uther(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.holyPower = 0
    def attack(self):
        if self.holyPower > 10:
            self.health += 10
            self.holyPower = 0
        else:
            self.holyPower += random.randint(1, 3)
        return random.randint(1, self.attack_power) * 1.25

    def take_damage(self, damage):
        self.health -= damage / 2
        # TODO We should prevent the paladins health from going into the NEGATIVE
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage / 2} damage. Health is now {self.health}.")