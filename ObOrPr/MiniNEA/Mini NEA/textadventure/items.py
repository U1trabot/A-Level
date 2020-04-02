import sys, time, random
from textadventure.questions import Question

def type(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")
    sys.stdout.flush()

class Item:
    """Parent Class For All Items"""
    def __init__(self,name,value,description,type):
        self.name = name #Name Of Item
        self.value = value #How Much An Item Is Worth
        self.description = description #Description Of Item
        self.type = type #What Type Of Item It Is
    def get_name(self):
        """Returns Name Attribute Of Item Object"""
        return self.name
    def get_value(self):
        """Returns Value Attribute Of Item Object"""
        return self.value
    def get_description(self):
        """Returns Description Attribute Of Item Object"""
        return self.description
    def get_type(self):
        """Returns Type Attribute Of Item Object"""
        return self.type
    def set_name(self,name):
        """Sets The Name Of The Item Object"""
        self.name = name
    def set_value(self,value):
        """Sets The Value Of The Item Object"""
        self.value = value
    def set_description(self,description):
        """Sets The Description Of The Item Object"""
        self.description = description
    def set_type(self,type):
        """Sets The Type Of The Item Object"""
        self.type = type
    def itemInfo(self,place):
        """Outputs Information About Itself"""
        type("There is a"+" "+self.type+" "+"in this"+" "+place)
        type("=-----------------------=")
        type(self.description)
        print()
    def invOutput(self):
        """Outputs Inventory Version Of Information About Itself"""
        type("Name: "+self.name)
        type("Description: "+self.description)
        type("Value: "+str(self.value))
        type("Type: "+self.type)
class Weapon(Item):
    """Item Sub-class Used For Fighting"""
    def __init__(self,name,value,description,type,damageType,hands,damage):
        super().__init__(name,value,description,"Weapon") #Calls Parent __init__
        self.damageType = damageType #The Type Of Damage The Weapon Deals
        self.weaponType = type #The Type Of Weapon It Is
        self.hands = hands #The Number Of Hands Needed To Use The Weapon
        self.damage = damage #The Maximum Damage The Weapon Can Deal
    def get_damageType(self):
        """Returns Damage Type Attribute Of Weapon Object"""
        return self.damageType
    def get_WeaponType(self):
        """Returns Weapon Type Attribute Of Weapon Object"""
        return self.WeaponType
    def get_hands(self):
        """Returns Number Of Hands Attribute Of Weapon Object"""
        return self.hands
    def set_damageType(self,damageType):
        """Sets Damage Type Attribute Of Weapon Object"""
        self.damageType = damageType
    def set_weaponType(self,weaponType):
        """Sets Weapon Type Attribute Of Weapon Object"""
        self.weaponType = weaponType
    def set_hands(self,hands):
        """Returns Number Of Hands Attribute Of Weapon Object"""
        self.hands = hands
    def attack(self):
        """Generates Questions Based On Damage Type, And Returns Damage Value Depending On If The Question Was Answered Correctly"""
        if self.damageType.lower() == "addition":
            if Question().addition():
                return random.randint(round(self.damage/2),self.damage)
            else:
                return random.randint(0,round(self.damage/10))
        elif self.damageType.lower() == "subtraction":
            if Question().subtraction():
                return random.randint(round(self.damage/2),self.damage)
            else:
                return random.randint(0,round(self.damage/10))
        elif self.damageType == "negatives":
            if random.randint(0,1) == 1:
                if Question().negToBin():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
            else:
                if Question().binToNeg():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
        elif self.damageType.lower() == "fixed":
            if random.randint(0,1) == 1:
                if Question().fixToBin():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
            else:
                if Question().binToFixed():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
        elif self.damageType.lower() == "floating":
            if random.randint(0,1) == 1:
                if Question().floatToBin():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
            else:
                if Question().binToFloat():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
        elif self.damageType.lower() == "facts":
            if Question().multipleChoice():
                return random.randint(round(self.damage/2),self.damage)
            else:
                return random.randint(0,round(self.damage/10))
        elif self.damageType.lower() == "conversion":
            num = random.randint(0,5)
            if num == 0:
                if Question().decToBinConv():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
            elif num == 1:
                if Question().binToDecConv():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
            elif num == 2:
                if Question().decToHexConv():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
            elif num == 3:
                if Question().hexToDecConv():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
            elif num == 4:
                if Question().binToHexConv():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
            elif num == 5:
                if Question().hexToBinConv():
                    return random.randint(round(self.damage/2),self.damage)
                else:
                    return random.randint(0,round(self.damage/10))
    def invOutput(self):
        """Override For Item InvOutput To Output Weapon Attributes Aswell"""
        type("Name: "+self.name)
        type("Description: "+self.description)
        type("Value: "+str(self.value))
        type("Type: "+self.weaponType)
        type("Damage Type: "+self.damageType.title())
        type("Number Of Hands: "+str(self.hands))
        type("Max Damage: "+str(random.randint(round(self.damage/2),self.damage)))
class Potion(Item):
    """Item Sub-class Used For Health Potions"""
    def __init__(self,name,value,description,health):
        super().__init__(name,value,description,"Health Potion") #Calls Parent Init, Sets Type To Health Potion
        self.health = health #The Maximum Health The Potion Can Heal
    def use(self):
        """Returns A Half-Random Health Value Based On The Health Attribute"""
        return random.randint(round(self.health/2),self.health)