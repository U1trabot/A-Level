import gps, items, npcs, sys, time, random

def type(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")
    sys.stdout.flush()
def type2(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    sys.stdout.write("\n")
    sys.stdout.flush()

class Player:
    def __init__(self):
        self.health = 100
        self.inventory = {}
        self.equipedWeapon = None
        self.dead = False
        self.victorious = False
        self.location = None
        self.score = 0
    def move(self,location):
        self.location = location

yeetRoom = gps.Location("The Grand Hall Of Yeet","an ornate hall with the word 'yeet' spray painted on the walls")
yeet1 = items.Item("Dude Item 1",99,"A item of a dude","Trinket")
yeet2 = items.Item("Dude Item 2",97,"A second item of a dude","Trinket")
yeet3 = items.Item("Dude Item 3",98,"A third item of a dude","Trinket")
yeet4 = items.Weapon("Dude Weapon",97,"The sword of the true dude","Sword","negatives",1,21)
dude = npcs.NPC("Dude","A normal dude")
dude.additem(yeet1)
dude.additem(yeet3)
dude.additem(yeet4)
dude.addline("La la lala la laa, just a boring dude")
scary = npcs.Enemy("Darth Batula","An Evil Vampire Bat",10,5)
scary.addline("I am darth batula, ha ha ha haaaa")
yeetRoom.link_npc(dude,"dude")
yeetRoom.link_item(yeet2,"small trinket")
yeetRoom.link_npc(scary,"bat")
place2 = gps.Location("The Cave I Guess","a dark and gloomy cave")
yeetRoom.link_location(place2,"cave","hall")


player  = Player()
player.move(yeetRoom)
fists = items.Weapon("Bare Knuckles",0,"Your fists","Unarmed","conversion",2,4)
player.equipedWeapon = fists

def play():
    if player.health <= 0:
        player.dead = True
    command = input("> ")
    commands = command.split(' ')
    if commands[0].lower() == "goto":
        if len(commands) == 2:
            player.move(player.location.goto(commands[1]))
        elif len(commands) > 2:
            type("Too Many Arguments For Goto. Only 1 Expected")
            play()
        else:
            type("Goto where?")
            play()
    elif commands[0].lower() == "talkto":
        if len(commands) == 2:
            try:
                player.location.connectedNPCs[commands[1]].speak()
            except:
                type("Wait who is the "+commands[1]+"?")
        elif len(commands) > 2:
            type("Too Many Arguments For Talk. Only 1 Expected")
            play()
        else:
            type("Talk to who?")
            play()
    elif commands[0].lower() == "inv":
        if len(commands) == 1:
            type("=-----Player's Inventory -----=")
            print()
            for item in player.inventory:
                player.inventory[item].invOutput()
                print()
            type("=-----------------------------=")
        else:
            type("Too Many Arguments For Inv, None Expected")
            play()
    elif commands[0].lower() == "stealfrom":
        if len(commands) == 2:
            try:
                print()
                player.location.connectedNPCs[commands[1]].outputInv()
                print()
                type("What would you like to steal?")
                item = input("> ").title()
                stolen = player.location.connectedNPCs[commands[1]].steal(item)
                if stolen is not None:
                    player.inventory[item] = stolen
            except:
                type("Wait who is the "+commands[1]+"?")
        elif len(commands) > 2:
            type("Too Many Arguments For Steal, 1 Expected")
            play()
        else:
            type("Steal from who? ")
            play()
    elif commands[0].lower() == "take":
        if len(commands) > 1:
            argument = []
            for word in commands:
                if word != commands[0]:
                    argument.append(word)
            argument = " ".join(map(str,argument))
            if argument in player.location.connectedItems:
                player.inventory[argument] = player.location.connectedItems.pop(argument)
                type("You take the "+argument.title())
            else:
                type("There is no "+argument.title()+" here")
        else:
            type("Take what?")
    elif commands[0].lower() == "fight":
        if len(commands) == 2:
            if commands[1] in player.location.connectedNPCs:
                enemy = player.location.connectedNPCs[commands[1]]
                if isinstance(enemy, npcs.Enemy):
                    while player.health > 0 and enemy.health > 0:
                        type("Your Health ["+str(player.health)+"]")
                        type("Their Health ["+str(enemy.health)+"]")
                        print()
                        type2("You swing to attack!")
                        hit = player.equipedWeapon.attack()
                        print()
                        enemy.health -= hit
                        type2("You dealt "+str(hit)+" damage!")
                        print()
                        if random.randint(0,1) == 1:
                            type2("The enemy attacks you!")
                            hit = enemy.attack()
                            player.health -= hit
                            type2("You took "+str(hit)+" damage!")
                            print()
                    if player.health <= 0:
                        player.dead = True
                        type2("You died, Game Over")
                    elif enemy.health <= 0:
                        type2("The enemy has been defeated!")
                        player.score += round((enemy.health+enemy.damage)/2)
                        type("Your score is now "+str(player.score))
                else:
                    type("You shouldn't kill civilians")
            else:
                type("Who is that?")
        elif len(commands) > 2:
            type("Too many arguments for Fight, Expected 1")
            play()
        else:
            type("Fight who?")
            play()
    elif commands[0].lower() == "help":
        type("Commands:")
        type("goto : move to a location")
        type("talkto : talk to an npc")
        type("inv : view your inventory")
        type("stealfrom : steal from an npc")
        type("fight : fight with an enemy npc")
        type("help : view this command list")
    print()
type("Use help to view commands")
print()
while not player.dead and not player.victorious:
    player.location.info()
    play()