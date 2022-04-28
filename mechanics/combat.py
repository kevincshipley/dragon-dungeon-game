'''
A great hero sets forth on their quest...
'''

print(__doc__)

import random
from random import randint

d4 = randint(1, 4)
d6 = randint(1, 6)
d8 = randint(1, 8)
d10 = randint(1, 10)
d12 = randint(1, 12)
d20 = randint(1, 20)

# Player chooses their weapon/class
weapon = input("Choose your weapon: dagger, bow, sword, magic: ")

if weapon == "dagger":
    damage = d4
    health = 6
    attack = 2
    armor = 12
elif weapon == "bow":
    damage = d6
    health = 8
    attack = 1
    armor = 12
elif weapon == "sword":
    damage = d8
    health = 8
    attack = 0
    armor = 10
elif weapon == "magic":
    damage = d12
    health = 6
    attack = 0
    armor = 10
elif weapon == "BFG":
    damage = d20
    health = 100
    attack = 100
    armor = 100
else:
    weapon = input("Invalid weapon.")
    quit()

print("You ready your", weapon, "for adventure.")

# while moster_hp > 0:
# fight continues

# a random enemy is selected
enemies = ["goblin", "owlbear", "dragon", "troll"]
monster = random.choice(enemies)

if monster == "goblin":
    monarmor = 10
    monhp = 4
    monattack = d4
if monster == "owlbear":
    monarmor = 13
    monhp = 8
    monattack = d6
if monster == "dragon":
    monarmor = 18
    monhp = 12
    monattack = d8
if monster == "troll":
    monarmor = 8
    monhp = 12
    monattack = d6

print("\nA terrifying {} appears!".format(monster))

while monhp >0:
    input("Press ENTER to attack.")
    # Player attacks the monster
    # check to see if attack hits, then roll damage if hits
    hit = d20 + attack
    print()
    if hit == 20:
        attackdamage = damage * 2
        print("CRITICAL HIT!!!"
              "\nYou hit the {} with your {} for {} damage!".format(monster,
                                                              weapon, damage))
        monhp = monhp - attackdamage
    elif hit >= monarmor:
        attackdamage = damage
        print("You hit the {} with your {} for {} damage!".format(monster,
                                                              weapon, damage))
        monhp = monhp - attackdamage
    else:
        print("You miss the {} with your {}".format(monster, weapon))
        
    # if monster dies, ends
    if monhp <= 0:
        print("You have slain the {}!".format(monster))\
                   
    # the monster attacks back if still alive
    elif monhp > 0:
        input("\nThe {} attacks...".format(monster))
        if d20 >= armor:
            playerdamage = monattack
            health = health - playerdamage
            print("The {} hits for {} damage".format(monster, playerdamage))
        else:
            print("The {} misses!".format(monster))
    
    # print player health
    if health > 0:
        print("\nYou have {} hp left.".format(health))
    else:
        monhp = 0
    attack += 1
    monattack += 1

if health > 0:
    print("\nVictory is yours!")
else:
    print("\nYou have been slain...")
