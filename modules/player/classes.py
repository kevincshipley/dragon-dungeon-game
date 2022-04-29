class Class:
    def __init__(self, name="Peasant", attack=0, armor=0, health=1):
        self.name = name
        if name == "Rogue":
            self.setAttack(3)
            self.setArmor(12)
            self.setHealth(10)
        elif name == "Ranger":
            self.setAttack(2)
            self.setArmor(12)
            self.setHealth(12)
        elif name == "Warrior":
            self.setAttack(1)
            self.setArmor(14)
            self.setHealth(14)
        elif name == "Wizard":
            self.setAttack(0)
            self.setArmor(10)
            self.setHealth(10)
        else:
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
        if health > 0:
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

##player = Class()
##
##print("You're a", player.getName())
##print("Attack:", player.getAttack())
##print("Armor:", player.getArmor())
##print("Health:", player.getHealth())
##
##input("\nPress ENTER to continue...\n")
##
##player = Class("Rogue")
##
##print("You're a", player.getName())
##print("Attack:", player.getAttack())
##print("Armor:", player.getArmor())
##print("Health:", player.getHealth())
##
##input("\nPress ENTER to continue...\n")
##
##player = Class("Ranger")
##
##print("You're a", player.getName())
##print("Attack:", player.getAttack())
##print("Armor:", player.getArmor())
##print("Health:", player.getHealth())
##
##input("\nPress ENTER to continue...\n")
##
##player = Class("Warrior")
##
##print("You're a", player.getName())
##print("Attack:", player.getAttack())
##print("Armor:", player.getArmor())
##print("Health:", player.getHealth())
##
##input("\nPress ENTER to continue...\n")
##
##player = Class("Wizard")
##
##print("You're a", player.getName())
##print("Attack:", player.getAttack())
##print("Armor:", player.getArmor())
##print("Health:", player.getHealth())
##
##input("\nPress ENTER to continue...\n")
