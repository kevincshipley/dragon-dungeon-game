from modules.mechanics import dice

print(dice.d4.roll(), "\n")

from modules.player import classes

player = classes.Class("Wizard")

print("You're a", player.getName())
print("Attack:", player.getAttack())
print("Armor:", player.getArmor())
print("Health:", player.getHealth())
