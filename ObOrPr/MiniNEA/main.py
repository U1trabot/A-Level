import gps, items, npcs, sys, time, random, getpass

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


file = open("data.txt","a+")
file.close()

type("Welcome to the text adventure what is your username?")
username = input("> ")
found= False
x = 0
file = open("data.txt","r")
database = []
for line in file:
    line = line.split("kyuip")
    if line[0].lower() == username.lower():
        found = True
        location = x
    database.append([line[0],line[1]])
    x += 1
file.close()
if found:
    type("What is your password?")
    password = getpass.getpass("> ")
    if password == database[location][1].rstrip():
        type("Welcome To The Text adventure")
    else:
        type("Invalid Login")
        exit()
else:
    type("Username not in database, do you want to create an account? (Y/N)")
    answer = input("> ")
    if answer.lower() == "y":
        type("What do you want your password to be?")
        password = getpass.getpass("> ")
        type("Please Confirm Password")
        password2 = getpass.getpass("> ")
        if password == password2:
            file = open("data.txt","a")
            file.write(username+"kyuip"+password+"\n")
        else:
            type("Passwords Do Not Match")
            exit()
    else:
        exit()
class Player:
    def __init__(self):
        self.health = 100
        self.inventory = {}
        self.equipedWeapon = None
        self.dead = False
        self.victorious = False
        self.location = None
        self.score = 0
        self.cash = 0
    def move(self,location):
        self.location = location

#========================================Object Creation Goes Below This Line============================================

#Make Objects Here

#========================================================================================================================

player  = Player()
player.move('STARTING_ROOM')
fists = items.Weapon("Bare Knuckles",0,"Your fists","Unarmed","conversion",2,4)
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
            if commands[1].lower() in player.location.connectedNPCs:
                print()
                player.location.connectedNPCs[commands[1].lower()].outputInv()
                print()
                type("What would you like to steal?")
                item = input("> ").title()
                stolen = player.location.connectedNPCs[commands[1].lower()].steal(item)
                if stolen is not None:
                    player.inventory[item] = stolen
                    type("You have stolen the "+stolen.get_name())
            else:
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
                item = player.location.connectedItems.pop(argument)
                player.inventory[item.get_name().title()] = item
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
                    StartingHealth = enemy.health
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
                        player.score += round((StartingHealth+enemy.damage)/2)
                        player.location.connectedNPCs.pop(commands[1])
                        type("Your score is now "+str(player.score))
                        if enemy.boss:
                            player.victorious = True
                            type("You have defeated the boss, you win!")
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
                type("You have equipped "+player.equipedWeapon.get_name())
            else:
                type("You do not have that weapon")
                play()
        else:
            type("Equip what?")
            play()
    elif commands[0].lower() == "sellto":
        if len(commands) > 1:
            argument = []
            for word in commands:
                if word != commands[0]:
                    argument.append(word)
            commands[1] = " ".join(map(str,argument)).title()
            if commands[1].lower() in player.location.connectedNPCs:
                npc = player.location.connectedNPCs[commands[1].lower()]
                if isinstance(npc, npcs.Merchant):
                    type("=-----Player's Inventory -----=")
                    print()
                    for item in player.inventory:
                        player.inventory[item].invOutput()
                        print()
                    type("=-----------------------------=")
                    type("What item do you want to sell?")
                    item = input("> ")
                    if item.title() in player.inventory:
                        price = npc.sell(player.inventory.pop(item.title()))
                        player.cash += price
                    else:
                        type("You do not have that item!")
                else:
                    type("You cannot sell to this person")
                    play()
            else:
                type("I don't see a "+commands[1].title())
        else:
            type("Sell to who?")
            play()
    elif commands[0].lower() == "bal":
        type("You have "+str(player.cash)+"₿")
    elif commands[0].lower() == "buyfrom":
        if len(commands) > 1:
            argument = []
            for word in commands:
                if word != commands[0]:
                    argument.append(word)
            commands[1] = " ".join(map(str,argument)).title()
            if commands[1].lower() in player.location.connectedNPCs:
                npc = player.location.connectedNPCs[commands[1].lower()]
                if isinstance(npc, npcs.Merchant):
                    npc.outputInv()
                    type("[Balance]: "+str(player.cash)+"₿")
                    type("What would you like to buy? ")
                    item = input("> ").title()
                    if item in npc.inventory:
                        if npc.inventory[item].get_value() <= player.cash:
                            player.cash -= npc.inventory[item].get_value()
                            player.inventory[item] = npc.inventory.pop(item)
                            type("You have bought the "+player.inventory[item].get_name())
                        else:
                            type("You cannot afford that item!")
                    else:
                        type("That item is not for sale")
                else:
                    type("You cannot buy from this person")
                    play()
            else:
                type("I don't see a "+commands[1].title())
        else:
            type("Buy from who?")
            play()
    elif commands[0].lower() == "drink":
        if len(commands) > 1:
            argument = []
            for word in commands:
                if word != commands[0]:
                    argument.append(word)
            argument = " ".join(map(str,argument)).title()
            if argument in player.inventory:
                item = player.inventory.pop(argument)
                if isinstance(item, items.Potion):
                    regen = item.use()
                    type("You heal "+str(regen)+" health")
                    player.health += regen
                    type("You drink the "+argument.title())
                    if player.health > 100:
                        player.health = 100
                else:
                    type("You cannot drink that")
            else:
                type("You don't have a "+argument.title())
        else:
            type("Drink what?")
    elif commands[0].lower() == "health":
        type("You have "+str(player.health)+" health")
    elif commands[0].lower() == "help":
        type("Commands:")
        type("goto : move to a location")
        type("talkto : talk to an npc")
        type("inv : view your inventory")
        type("stealfrom : steal from an npc")
        type("fight : fight with an enemy npc")
        type("help : view this command list")
        type("equiped : shows you what weapon is currently equiped")
        type("equip : equip a weapon from your inventory")
        type("sellto : sell to a merchant npc")
        type("bal : view your current balance")
        type("buyfrom : buy items from a merchant")
        type("drink : drink a potion to restore health")
        type("health : view your current health")
    print()
type("Use help to view commands, By default answers are 8 bit")
print()
while not player.dead and not player.victorious:
    player.location.info()
    try:
        for npc in player.location.connectedNPCs:
            if isinstance(player.location.connectedNPCs[npc], npcs.Enemy):
                if player.location.connectedNPCs[npc].ambush:
                    type("You are attacked by "+player.location.connectedNPCs[npc].get_name()+" the "+npc)
                    print()
                    enemy = player.location.connectedNPCs[npc]
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
                        player.location.connectedNPCs.pop(npc)
                        type("Your score is now "+str(player.score))
    except:
        pass
    play()
name = username
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
    file.write(score[0]+","+score[1]+"\n")
file.close()
