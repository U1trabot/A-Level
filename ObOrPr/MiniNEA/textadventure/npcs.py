import sys,time,random

def type(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")
    sys.stdout.flush()

class NPC:
    """Parent Class For All Non-Player Characters"""
    def __init__(self,name,description):
        self.name = name #The Name Of The NPC
        self.description = description #A Description Of The NPC
        self.conversation = [] #The Lines Of Conversation The NPC Can Say
        self.inventory = {} #A Dictionary To Contain What Items The NPC Has
    def get_name(self):
        """Returns Name Attribute Of NPC Object"""
        return self.name
    def get_description(self):
        """Returns Description Attribute Of NPC Object"""
        return self.description
    def set_name(self,name):
        """Sets Name Attribute Of NPC Object"""
        self.name = name
    def set_description(self,description):
        """Sets Description Attribute Of NPC Object"""
        self.description = description
    def addline(self,line):
        """Adds A Conversation Line To The Array"""
        self.conversation.append(line)
    def additem(self,item):
        """Adds An Item Object To The Inventory Dictionary"""
        self.inventory[item.get_name()] = item
    def outputInv(self):
        """Outputs The NPC's Inventory"""
        type("=-----"+self.name+"'s Inventory -----=")
        for item in self.inventory:
            self.inventory[item].invOutput()
            print()
        line = ["-" for char in range(len("=-----"+self.name+"'s Inventory -----=")-2)]
        type("="+"".join(map(str,line))+"=")
    def steal(self,item):
        """Returns And Pops A Stolen Item Object"""
        if item in self.inventory:
            return self.inventory.pop(item)
        else:
            type("They do not have that item")
            return None
    def speak(self):
        """Outputs The Conversation Array"""
        for line in self.conversation:
            type("["+self.name+"]: "+line)
class Enemy(NPC):
    """NPC Sub-class Used For People That Fight The Player"""
    def __init__(self,name,description,health,damage,ambush=False,boss=False):
        super().__init__(name,description) #Calls Parent __init__
        self.health = health #The Health Of The Enemy
        self.damage = damage #The Maximum Damage The Enemy Can Deal
        self.ambush = ambush #Whether Or Not The Enemy Will Attack The Player By Themselves
        self.boss = boss #Wether Or Not This Enemy Is The Final Boss
    def set_health(self,health):
        """Sets Health Attribute Of Enemy Object"""
        self.health = health
    def set_damage(self, damage):
        """Sets Damage Attribute Of Enemy Object"""
        self.damage = damage
    def get_health(self):
        """Returns Health Attribute Of Enemy Object"""
        return self.health
    def get_damage(self):
        """Returns Damage Attribute Of Enemy Object"""
        return self.damage
    def hurt(self,damage):
        """Reduces The Enemy's Health By A Given Amount"""
        self.health -= damage
    def attack(self):
        """Returns A Half-Random Damage Value Based On The Damage Attribute"""
        return random.randint(round(self.damage/2),self.damage)
class Merchant(NPC):
    """NPC Sub-class Used For People Who Can Be Traded With"""
    def __init__(self,name,description):
        super().__init__(name,description) #Calls Parent __init__
        self.name += " the merchant" #Changes Name To Contain "The Merchant"
    def sell(self,item):
        """Outputs A Confirmation Of An Item Being Sold, And Returns Item Value"""
        type("You sell your "+item.get_name()+" to "+self.name)
        print()
        return item.get_value()
    def steal(self,item):
        """Overrides The NPC Steal Method So That Merchants Cannot Be Stolen From"""
        type("You cannot steal from merchants")
        return None