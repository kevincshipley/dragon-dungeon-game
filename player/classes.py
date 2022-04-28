class Class:
    def __init__(self, name: str, attack: int, armor: int, health:int):
        self.name = name
        self.attack = attack
        self.armor = armor
        self.health = health
    # set stats and class name
    def setName(self, name):
        self.name = name
    def setAttack(self, attack):
        self.attack = attack
    def setArmor(self, armor):
        if armor >= 0:
            self.armor = armor
    def setHealth(self, health):
        if healt > 0:
            self.health = health
    # get them now
    def getName(self):
        return self.name
    def getAttack(self):
        return self.attack
    def getArmor(self):
        return self.armor
    def getHealth(self):
        return self.health

peasant = Class("Peasant", 0, 0, 1)
rogue = Class("Rogue", 3, 12, 10)
ranger = Class("Ranger", 2, 12, 12)
warrior = Class("Warrior", 1, 14, 14)
wizard = Class("Wizard", 0, 10, 10)

player = wizard

print("You're a", player.getName())
print("Attack:", player.getAttack())
print("Armor:", player.getArmor())
print("Health:", player.getHealth())
