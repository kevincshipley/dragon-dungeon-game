import random
from random import randint

class Dice:
    def __init__(self, sides):
        self.sides = sides
    # return the number of sides of the die
    def getSides(self):
        return self.sides
    # set the number of sides of the dies
    def setSides(self, sides):
        if sides > 0:
            self.sides = sides 
    # roll the die
    def roll(self):
        return randint(1, self.sides)

# set the dice
d4 = Dice(4)
d6 = Dice(6)
d8 = Dice(8)
d10 = Dice(10)
d12 = Dice(12)
d20 = Dice(20)
d100 = Dice(100)
