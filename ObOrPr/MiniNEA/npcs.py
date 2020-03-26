import sys,time,random

def type(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")
    sys.stdout.flush()

class NPC:
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.conversation = []
        self.inventory = {}
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def set_name(self,name):
        self.name = name
    def set_description(self,description):
        self.description = description
    def addline(self,line):
        self.conversation.append(line)
    def additem(self,item):
        self.inventory[item.get_name()] = item
    def outputInv(self):
        type("=-----"+self.name+"'s Inventory -----=")
        for item in self.inventory:
            self.inventory[item].invOutput()
            print()
        line = ["-" for char in range(len("=-----"+self.name+"'s Inventory -----=")-2)]
        type("="+"".join(map(str,line))+"=")
    def steal(self,item):
        if item in self.inventory:
            return self.inventory.pop(item)
        else:
            type("They do not have that item")
            return None
    def speak(self):
        for line in self.conversation:
            type("["+self.name+"]: "+line)
class Enemy(NPC):
    def __init__(self,name,description,health,damage,ambush=False,boss=False):
        super().__init__(name,description)
        self.health = health
        self.damage = damage
        self.ambush = ambush
        self.boss = boss
    def set_health(self,health):
        self.health = health
    def set_damage(self, damage):
        self.damage = damage
    def get_health(self):
        return self.health
    def get_damage(self):
        return self.damage
    def hurt(self,damage):
        self.health -= damage
    def attack(self):
        return random.randint(round(self.damage/2),self.damage)
class Merchant(NPC):
    def __init__(self,name,description):
        super().__init__(name,description)
        self.name += " the merchant"
    def sell(self,item):
        type("You sell your "+item.get_name()+" to "+self.name)
        print()
        return item.get_value()
    def steal(self,item):
        type("You cannot steal from merchants")
        return None