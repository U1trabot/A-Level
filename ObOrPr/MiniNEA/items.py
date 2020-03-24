import sys, time, questions, random

def type(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")
    sys.stdout.flush()

class Item:
    def __init__(self,name,value,description,type):
        self.name = name
        self.value = value
        self.description = description
        self.type = type
    def get_name(self):
        return self.name
    def get_value(self):
        return self.value
    def get_description(self):
        return self.description
    def get_type(self):
        return self.type
    def set_name(self,name):
        self.name = name
    def set_value(self,value):
        self.value = value
    def set_description(self,description):
        self.description = description
    def set_type(self,type):
        self.type = type
    def itemInfo(self,place):
        type("There is a"+" "+self.type+" "+"in this"+" "+place)
        type("=-----------------------=")
        type(self.description)
        print()
    def invOutput(self):
        type("Name: "+self.name)
        type("Description: "+self.description)
        type("Value: "+str(self.value))
        type("Type: "+self.type)
class Weapon(Item):
    def __init__(self,name,value,description,type,damageType,hands,damage):
        super().__init__(name,value,description,"Weapon")
        self.damageType = damageType
        self.weaponType = type
        self.hands = hands
        self.damage = damage
    def get_damageType(self):
        return self.damageType
    def get_WeaponType(self):
        return self.WeaponType
    def get_hands(self):
        return self.hands
    def set_damageType(self,damageType):
        self.damageType = damageType
    def set_weaponType(self,weaponType):
        self.weaponType = weaponType
    def set_hands(self,hands):
        self.hands = hands
    def attack(self):
        if self.damageType.lower() == "addition":
            if questions.Question().addition():
                return random.randint(round(self.damage/2),self.damage)
            else:
                return random.randint(0,round(self.damage/10))
        elif self.damageType.lower() == "subtraction":
            if questions.Question().subtraction():
                return random.randint(round(self.damage/2),self.damage)
            else:
                return random.randint(0,round(self.damage/10))
        elif self.damageType == "negatives":
            if random.randint(0,1) == 1:
                if questions.Question().negToBin():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
            else:
                if questions.Question().binToNeg():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
        elif self.damageType.lower() == "fixed":
            if random.randint(0,1) == 1:
                if questions.Question().fixToBin():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
            else:
                if questions.Question().binToFixed():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
        elif self.damageType.lower() == "floating":
            if random.randint(0,1) == 1:
                if questions.Question().floatToBin():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
            else:
                if questions.Question().binToFloat():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
        elif self.damageType.lower() == "facts":
            if questions.Question().multipleChoice():
                return random.randint(round(self.damage/2),self.damage)
            else:
                return random.randint(0,round(self.damage/10))
        elif self.damageType.lower() == "conversion":
            num = random.randint(0,5)
            if num == 0:
                if questions.Question().decToBinConv():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
            elif num == 1:
                if questions.Question().binToDecConv():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
            elif num == 2:
                if questions.Question().decToHexConv():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
            elif num == 3:
                if questions.Question().hexToDecConv():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
            elif num == 4:
                if questions.Question().binToHexConv():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
            elif num == 5:
                if questions.Question().hexToBinConv():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
    def invOutput(self):
        type("Name: "+self.name)
        type("Description: "+self.description)
        type("Value: "+str(self.value))
        type("Type: "+self.weaponType)
        type("Damage Type: "+self.damageType.title())
        type("Number Of Hands: "+str(self.hands))
        type("Max Damage: "+str(random.randint(round(self.damage/2),self.damage)))