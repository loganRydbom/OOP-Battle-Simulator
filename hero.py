import random

class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        #TODO Set the hero's name.
        self.name = name
        #TODO Set the hero's health. You might give the hero more health than a paladin.
        self.health = 120
        #TODO Set the hero's attack power. Should it be more consistent than the paladin's?
        self.attackPower = 50
    

    def strike(self):
        # TODO Implement the hero's attack logic. It could be stronger or more consistent than a paladin's.
        return random.randint(1, self.attackPower)

    
    def receive_damage(self, damage):
        # TODO Implement take_damage
        # TODO We should prevent health from going into the NEGATIVE
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
    
    #TODO define is_alive
    def is_alive(self):
        return self.health > 0
