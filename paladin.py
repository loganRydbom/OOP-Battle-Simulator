import random
from enemy import Enemy

class Paladin(Enemy):
    """
    This is our paladin blueprint 
    
    Attributes:
        name: The name of the Paladin
        health: The current health value 
        rank: Where does the paladin stand in the Knights of the Silver Hand
    """
    def __init__(self, name, rank):
        super().__init__(name)
        self.color = rank
