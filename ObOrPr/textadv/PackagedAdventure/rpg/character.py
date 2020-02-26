import sys,time


def type(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")
    sys.stdout.flush()

class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        """Sets attributes for Character class"""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        """Outputs the name and description of a character for use in a room"""
        type(( self.name + " is here!" ))
        type( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        """Sets a character's conversation line"""
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        """Outputs a conversation line if there is one, if not tells player that the character does not want to talk to them"""
        if self.conversation is not None:
            type(("[" + self.name + " says]: " + self.conversation))
        else:
            type((self.name + " doesn't want to talk to you"))

    # Fight with this character
    def fight(self, combat_item):
        """Initaites a fight with the character, will always say doesn't want to fight you for a default character"""
        type((self.name + " doesn't want to fight with you"))
        return True
    def steal(self):
        """Initiates a steal from the character, will tell the player that they cannot steal from a default character"""
        type("You cannot steal from a neutral or friendly target")
    def hug(self):
        """Initiates a hug with a character, will tell player they cannot for a default character"""
        type("You cannot hug a neutral or enemy target")
class Enemy(Character):

    enemies_defeated = 0

    def __init__(self, char_name, char_description):
        """Creates attributes for Enemey class"""
        super().__init__(char_name, char_description)
        self.weakness = None
        self.item = None
    def fight(self, combat_item):
        """Initiates a fight with enemy, uses combat item to tell if fight is one, player wins = True, player loses = False"""
        if self.weakness == combat_item:
            type(("You killed"+" "+self.name+" "+"with the"+" "+combat_item))
            Enemy.enemies_defeated += 1
            return True
        else:
            type(("Your"+" "+combat_item+" "+"does little against the might of"+" "+self.name))
            return False
    def set_weakness(self,char_weakness):
        """Sets the weakness attribute"""
        self.weakness = char_weakness
    def get_weakness(self):
        """Returns the weakness attribute"""
        return self.weakness
    def set_item(self,new_item):
        """Sets the item attribute"""
        self.item = new_item
    def get_item(self):
        """Returns the item attribute"""
        return self.item
    def set_defeated(self,new_defeated):
        """Sets the enemies_defeated count"""
        Enemy.enemies_defeated = 0
    def get_defeated(self):
        """Returns the enemies_defeated count"""
        return Enemy.enemies_defeated
    def steal(self):
        """Initaites a steal from an Enemy, will only continue if Enemy has an item"""
        if self.item is not None:
            type(("You steal a"+" "+self.item.get_name()+" "+"from"+" "+self.name))
            return True
        else:
            type(self.name,"has nothing to steal")
            return False
class Friend(Character):
    def __init__(self, char_name, char_description):
        """Creates attributes for Friend class"""
        super().__init__(char_name, char_description)
        self.feeling = 0
    def hug(self):
        """Initaites a hug with the friend, will only work if feeling is above 10"""
        if self.feeling > 10:
            type((self.name+" "+"hugs you back"))
        else:
            type((self.name+" "+"doesn't want to hug you"))
    def set_feeling(self,feel):
        """Sets the feeling attribute"""
        self.feeling = feel
    def get_feeling(self):
        """Returns the feeling attribute"""
        return self.feeling