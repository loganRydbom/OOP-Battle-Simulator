import random
from enemy import Enemy

class Uther(Enemy):
    def attack(self):
        return random.randint(1, self.attack_power) * 1.25

    def take_damage(self, damage):
        self.health -= damage / 2
        # TODO We should prevent the paladins health from going into the NEGATIVE
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage / 2} damage. Health is now {self.health}.")