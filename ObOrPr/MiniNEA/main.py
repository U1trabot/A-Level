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
suicide = npcs.Enemy("Thanos","A strange purple man",100,69)
yeetRoom.link_npc(suicide,"purple man")
player  = Player()
player.move(yeetRoom)
fists = items.Weapon("Bare Knuckles",0,"Your fists","Unarmed","conversion",2,4)
god = items.Weapon("Op Weapon Of Doom",2,"A super op dev weapon","Mace","multipleChoice",2,1000000000)
yeetRoom.link_item(god,"large mace")
player.equipedWeapon = fists

def play():
    if player.health <= 0:
        player.dead = True
    command = input("> ")
    commands = command.split(' ')
    if commands[0].lower() == "goto":
        if len(commands) > 2:
            argument = []
            for word in commands:
                if word != commands[0]:
                    argument.append(word)
            commands[1] = " ".join(map(str,argument))
            player.move(player.location.goto(commands[1]))
        else:
            type("Goto where?")
            play()
    elif commands[0].lower() == "talkto":
        if len(commands) > 1:
            argument = []
            for word in commands:
                if word != commands[0]:
                    argument.append(word)
            commands[1] = " ".join(map(str,argument))
            try:
                player.location.connectedNPCs[commands[1]].speak()
            except:
                type("Wait who is the "+commands[1]+"?")
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
        if len(commands) >1:
            argument = []
            for word in commands:
                if word != commands[0]:
                    argument.append(word)
            commands[1] = " ".join(map(str,argument))
            try:
                print()
                player.location.connectedNPCs[commands[1].lower()].outputInv()
                print()
                type("What would you like to steal?")
                item = input("> ").title()
                stolen = player.location.connectedNPCs[commands[1].lower()].steal(item)
                if stolen is not None:
                    player.inventory[item] = stolen
            except:
                type("Wait who is the "+commands[1]+"?")
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
        if len(commands) > 1:
            argument = []
            for word in commands:
                if word != commands[0]:
                    argument.append(word)
            commands[1] = " ".join(map(str,argument))
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
                        player.location.connectedNPCs.pop(commands[1])
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
    elif commands[0].lower() == "equiped":
        type(player.equipedWeapon.get_name()+" is the currently equiped weapon.")
    elif commands[0].lower() == "equip":
        if len(commands) > 1:
            argument = []
            for word in commands:
                if word != commands[0]:
                    argument.append(word)
            commands[1] = " ".join(map(str,argument))
            if commands[1].title() in player.inventory:
                player.equipedWeapon = player.inventory[commands[1].title()]
            else:
                type("You do not have that weapon")
                play()
        else:
            type("Equip what?")
            play()
    elif commands[0].lower() == "help":
        type("Commands:")
        type("goto : move to a location")
        type("talkto : talk to an npc")
        type("inv : view your inventory")
        type("stealfrom : steal from an npc")
        type("fight : fight with an enemy npc")
        type("help : view this command list")
        type("equiped : shows you what weapon is currently equiped")
    print()
type("Use help to view commands")
print()
while not player.dead and not player.victorious:
    player.location.info()
    play()
if player.dead:
    type("What is your name?")
    name = input("> ")
    try:
        file = open('scoreboard.csv','x')
        file.close()
    except:
        pass
    finally:
        scoreboard = []
        file = open('scoreboard.csv','r')
        for line in file:
            line = line.split(',')
            line[1] = line[1].rstrip()
            scoreboard.append(line)
    sorted = []
    scoreboard.append([name,str(player.score)])
    while len(scoreboard) > 0:
        for item in scoreboard:
            count = 0
            for item2 in scoreboard:
                if int(item[1]) >= int(item2[1]):
                    count += 1
            if count == (len(scoreboard)):
                scoreboard.remove(item)
                sorted.append(item)
    for score in sorted:
        type(score[0]+": "+score[1])
    file.close()
    file = open('scoreboard.csv','w')
    for score in sorted:
        file.write(score[0]+","+score[1])
    file.close()
