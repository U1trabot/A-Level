from textadventure import * #Imports Text Adventure Modules
import sys,time,getpass,random #Imports Other Required Modules

def type(string): #Creates Function For Outputting Letter By Letter
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")
    sys.stdout.flush()
def type2(string): #Same As Above Function Just Slower
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    sys.stdout.write("\n")
    sys.stdout.flush()


file = open("data.txt","a+") #Creates Data.txt If It Doesn't Already Exist
file.close()

type("Welcome to the text adventure what is your username?") #Runs Login/Account Creation
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
class Player: #Creates Class To House Player Attriubtes
    def __init__(self):
        self.health = 100 #The Health Of The Player, Max 100
        self.inventory = {} #The Dictionary Of The Player's Items
        self.equipedWeapon = None #The Currently Equipped Weapon
        self.dead = False #Whether Or Not The Player Is Dead
        self.victorious = False #Whether Or Not The Player Has Defeated The Final Boss
        self.location = None #The Player's Current Locations
        self.score = 0 #The Player's Score
        self.cash = 0 #The Player's Money
    def move(self,location): #Method For Chaning Location Attribute
        self.location = location

#========================================Object Creation Goes Below This Line============================================

#Wild Plains
WildPlains = Location("Wild Plains", "A large expanse of land covered with overgrowth; with blades of grass that reach your knees. You suspect there are at least one hundred species of insects living amongst the grass and there is a potent smell of dirt and plants.")
LostDog = NPC("Lost Dog", "A sweet little dog.")
LostDog.addline("Woof!")
Bandit = Enemy("Bandit","A man who will will try to steal your money.",15,4)
LostChange = Item("Lost Change", 3, "Three Gold Coins Left By An Unlucky Traveller", "Coins")
WildPlains.link_npc(LostDog,"dog")
WildPlains.link_npc(Bandit,"bandit")
WildPlains.link_item(LostChange,"collection of coins")

#Flower Plains
FlowerPlains = Location("Flower Plains", "A fabulous area of green coated with wonderful flowers of all different colours. Owned by the city of kymar, this area of fields has been gardened to perfection. There is not a spot on the ground where you can’t see a beautiful flower has been grown.")
KymarGuard1 = NPC("Kymar Gaurd","Just a normal guard of Kymar City")
KymarGuard1.addline("Move Along")
GuardBadge = Item("Guard Badge", 10, "A Badge Used To Show The Employment As A Guard", "Badge")
KymarGuard1.additem(GuardBadge)
Gardener = NPC("Scruffy Gardener","A scruffy looking gardener who is busy tending to some flowers.")
Gardener.addline("Roses Look Wonderful In The Sunlight")
GardenRake = Item("Garden Rake", 2,"A Simple Rake Used To Tend The Flower Plains", "Tool")
Gardener.additem(GardenRake)
Tourist1 = NPC("Tourist", "A woman wearing foreign clothes admiring the surrounding flowers")
Tourist1.addline("I’ve never seen these many flowers before")
FlowerPlains.link_npc(KymarGuard1,"guard")
FlowerPlains.link_npc(Gardener,"gardener")

#Jonak City
LowerDistrict = Location("Jonak City | Lower District", "The poorest section of Jonak City, most manual labour is done by the citizens of this sector. The only part to have any money poured into it is the road that leads to the richer districts. There is a disgusting smell of animal waste as cattle do their business on the side of the road.")
Beggar = NPC("Beggar", "A very poor man begging for money since he seems to have none.")
Beggar.addline("Please, can you spare a coin?")
SpareChange = Item("Spare Change", 1, "A Coin Gifted To A Beggar", "Coin")
Beggar.additem(SpareChange)
PoorCitizen = NPC("Poor Citizen","A poor citizen tending to their farm, their only source of income.")
PoorCitizen.addline("Hopefully this year will yield a good harvest")
JonakGuard1 = NPC("Jonak Guard","Just a normal guard of Jonak City.")
JonakGuard1.addline("Move Along")
Thug = Enemy("Thug","Just A Mean Thug",5,5)
LowerDistrict.link_npc(Beggar,"beggar")
LowerDistrict.link_npc(PoorCitizen, "poor citizen")
LowerDistrict.link_npc(JonakGuard1, "guard")

CentreDistrict = Location("Jonak City | Centre District", "The largest section of Jonak City, home to the middle class and the hub for almost all trade within the city. Although there is lots of money being made in this district, the majority of its inhabitants are the employees of these rich trade businesses.")
JonakGuard2 = NPC("Jonak Guard", "Just a normal guard of Jonak City")
JonakGuard2.addline("Move Along")
Citizen1 = NPC("Citizen","A normal citizen going to buy their weekly supplies.")
Citizen1.addline("I’ve got quite a busy day today")
Frank = Merchant("Frank", "A humble merchant willing to trade all for just a little coin.")
HonedBlade = Weapon("Honed Blade", 50, "A One-Handed Sword, Forged To Near Perfection And Made Out Of Steel.","Sword","subtraction",1,10)
ElvenWarhammer = Weapon("Elven Warhammer", 100, "A Large Hammer Made Out Of Elven Steel. Perfect For Cracking A Few Skeletons Apart.", "Hammer", "facts", 2, 20)
GrandHealthPotion = Potion("Grand Health Potion", 30, "A Large Health Potion That Can Be Used To Heal Someone", 50)
Frank.additem(HonedBlade)
Frank.additem(ElvenWarhammer)
Frank.additem(GrandHealthPotion)
CentreDistrict.link_npc(JonakGuard2, "guard")
CentreDistrict.link_npc(Citizen1, "citizen")
CentreDistrict.link_npc(Frank, "merchant")

UpperDistrict = Location("Jonak City | Upper District", "The richest section of Jonak City. Home to Jonak’s Richest, this district if the most tantalising to look at. There are statues here, mansions there. A fancy water feature on every path and in every park. You notice that very little work in actually done in this district as it is likely made down in the lower sections.")
RichCitizen = NPC("Rich Citizen", "A rich citizen of Jonak, wearing much fancier clothes then most could ever dream of.")
RichCitizen.addline("Please stay away, I don’t want you dirtying my cloak.")
LargeGemstone = Item("Large Gemstone", 200, "A Fancy Gemstone, Probably Worth Quite A Bit To A Merchant", "Gemstone")
RichCitizen.additem(LargeGemstone)
Entertainer = NPC("Entertainer", "A centre district citizen trying to earn money by entertaining those with more money than him.")
EliteJonakGuard = NPC("Jonak Guard","A more weaponised version of the normal Jonak guard.")
EliteJonakGuard.addline("Move Along")
UpperDistrict.link_npc(RichCitizen,"rich citizen")
UpperDistrict.link_npc(Entertainer, "entertainer")
UpperDistrict.link_npc(EliteJonakGuard, "elite guard")

#Dragon Claw Dungeon
Corridor = Location("Dragon Claw Dungeon | The Corridor", "A dark stone Corridor lit by the shine of the moon or sun outside. You see your shadow cast on the floor beneath as you walk through the entrance of Dragon Claw Dungeon.")
Spider = Enemy("Spider","A small spider, likely harmless",2,1)
Corridor.link_npc(Spider,"spider")

WesternPassage = Location("Dragon Claw Dungeon | Western Passage", "A simple passageway to the west of the corridor, made from the same bleak stone as the rest of the dungeon.")

WesternSideRoom = Location("Dragon Claw Dungeon | Western Side-Room", "A small stone room, home to more bats and skeletons than actual treasure.")
Skeleton1 = Enemy("Skeleton","One Bony Boy",30,5,True)
Skeleton2 = Enemy("Skeleton","A Skeleton, With A Sword, And A Lust For Flesh",30,5,True)
WesternSideRoom.link_npc(Skeleton1,"little skeleton")
WesternSideRoom.link_npc(Skeleton2,"big skeleton")

EasternPassage = Location("Dragon Claw Dungeon | Eastern Passage","A passageway to the east of the corridor. There doesn’t seem to be anything important in this room. Unless... What’s that behind you?")
Ghost = Enemy("Ghost","A Spooky Ghost, Very Spooky",3,30,True)
EasternPassage.link_npc(Ghost,"ghost")

EasternSideRoom = Location("Dragon Claw Dungeon | Eastern Side-Room", "A small room with a torch in it that seems to burn forever. It is one of the only rooms in the dungeon to have its own lighting and yet there is no warmth coming from the flame. There is some loot here though.")
StaffOfLightning = Weapon("Staff Of Lightning",50,"A Grand Staff With A Small Clear Ball Rested In The Top Of It. Inside Of The Ball You Can See Streaks Of Electricity Arch Across The Surfaces.","Staff","addition",2,15)
Emerald = Item("Emerald",45,"A Pretty Little Gem. Green In Colour, And Likely Worth Lots Of Gold.","Gemstone")
EasternSideRoom.link_item(StaffOfLightning,"staff")
EasternSideRoom.link_item(Emerald,"emerald")

GreatHall = Location("Dragon Claw Dungeon | The Great Hall", "A long hall made mostly out of oak wood. You reckon that this dungeon was previously someone’s house. Before, you know, they died and haunted the place forever.")
Bat = NPC("Bat", "A Sweet Little Bat, No Vampireness About This One")
Bat.addline("Squeak")
GreatHall.link_npc(Bat,"bat")

BrokenBallroom = Location("Dragon Claw Dungeon | The Broken Ballroom", "A grand and luxurious ballroom, with a cracked marble floor and ripped curtains hanging over walls even though they lack windows. There is a sword rack on one of the walls.")
Zombie = Enemy("Zombie","Brains. Braaaaains. Braains.",20,20,True)
AncientSword = Weapon("Ancient Sword",30,"An Old Sword Left On A Sword Rack. You Cannot Be Sure What Race This Sword Was Made By. Perhaps A Race That Doesn’t Walk The Planet Anymore.","Sword","negatives",1,12)
BrokenBallroom.link_npc(Zombie,"zombie")
BrokenBallroom.link_item(AncientSword,"sword")

WindingStaircase = Location("Dragon Claw Dungeon | Winding Staircase", "A mesmerising spiral staircase that seems to infinitely descend deeper into the dungeon. Bats fly past your face as you follow the cracked stone steps and you swear you can hear a noise coming from the room below.")
VampireBat1 = Enemy("Vampire Bat","Bat + Vampire = Hungry For Blood",5,15,True)
WindingStaircase.link_npc(VampireBat1, "vampire bat")

DeepCellar = Location("Dragon Claw Dungeon | Deep Cellar", "A dark cellar lined with rotten wood. Although previously used to store wine and food, all that is left is rats and… bones?")
DisgruntledSkeleton = Enemy("Disgruntled Skeleton", "A Rather Angry Looking Skeleton, If That’s Even Possible",10,4,True)
FastRat = Enemy("Fast Rat", "A small rat with fast legs and sharp teeth",5,20,True)
RottenFood = Item("Rotten Food",0,"A Pile Of Disgusting Rotten Food, Nibbled Away By Rats","Junk")
DeepCellar.link_npc(DisgruntledSkeleton,"skeleton")
DeepCellar.link_npc(FastRat,"rat")
DeepCellar.link_item(RottenFood,"rotten food")

WesternTreasureRoom = Location("Dragon Claw Dungeon | Western Treasure Room", "A dimly lit room filled with treasure. Unless you have already looted the treasure, in which case the room is empty.")
BowOfAccurateShot = Weapon("Bow Of Accurate Shot",50,"A Keen Eye Is Still Needed To Use This Bow, But You May Find The Shots Land More Consistently Than Mundane Bows.","Bow","conversion",2,14)
WesternTreasureRoom.link_item(BowOfAccurateShot,"bow")

EasternTreasureRoom = Location("Dragon Claw Dungeon | Eastern Treasure Room","A small stone room with multiple circles of soot on the walls. It seems as if these spots where exposed to some kind of flame.")
FireballSpell = Weapon("Fireball Spell Book", 65, "A Spell Tome That Can Be Read To Cast Fireball At Will.","Spell Book","floating",2,18)
EasternTreasureRoom.link_item(FireballSpell,"spell book")

#The Deep Pit Dungeon
GreatFoyer = Location("The Deep Pit Dungeon | The Great Foyer","A large foyer with basalt walls. Strangely it gives the impression that this dungeon was designed to be just that, a dungeon.")
CrawlerZombie = Enemy("Crawler Zombie","A slow zombie, because this zombie has no legs.",10,20,True)
GreatFoyer.link_npc(CrawlerZombie, "zombie")

ElongatedCorridor = Location("The Deep Pit Dungeon | Elongated Corridor","A long corridor that connects to many rooms. One of the rooms, an arena, is connected by a very large entrance made of human bones. A very powerful enemy rests in that room, it may be wise not to disturb it until you are strong enough to fight it.")
MassivePotion = Potion("Massive Health Potion",20,"An Extremely Large Health Potion, Guaranteed To Bring You To Full Health.",200)
ElongatedCorridor.link_item(MassivePotion,"potion")

DarkSideRoom = Location("The Deep Pit Dungeon | Dark Side-Room","Other than the basalt walls that are shared with the rest of the dungeon. It seems that there is nothing special about this room. A waste of time really.")

RuinedTower = Location("The Deep Pit Dungeon | Ruined Tower", "A tower that used to stand great and tall. Unfortunately, the roof has since fallen in and there is no longer an elevation to the once great tower. Could be some treasure in the rubble though.")
VampireBat2 = Enemy("Count Batula", "The Famous Count Batula",25,32,True)
RuinedTower.link_npc(VampireBat2,"vampire bat")

ElvenPassageway = Location("The Deep Pit Dungeon | Elven Passageway","The only room in this dungeon not to have basalt walls. This passageway contains uniquely elven architecture. Pillars with diorite shafts, golden capitals and brass plinths.")
Rats = Enemy("A Mischief Of Rats","There are a lot of rats, looks deadly",60,3)
ElvenPassageway.link_npc(Rats,"bunch of rats")

DarkArena = Location("The Deep Pit Dungeon | The Dark Arena", "A sunken arena, home of the most fearsome creature housed in the deep pit dungeon, but also the rarest loot.")
LordHrungar = Enemy("Lord Hrungar","Only the final boss of the game, nothing massive.",150,20,True,True)
HrungarsBane = Weapon("Hrungar's Bane",666,"The Great-Sword Of The Mighty Lord Hrungar. Its Power Is More Than Any Mortal Could Imagine.","Greatsword","facts",2,50)
DarkArena.link_npc(LordHrungar,"devil man")
DarkArena.link_item(HrungarsBane,"greatsword")

SouthernLootRoom = Location("The Deep Pit Dungeon | Southern Loot Room","A small room filled with useless but likely valuable treasure. As you enter a sense of darkness washes over you.")
ShadowMonster = Enemy("Shadow Monster","A Monster made of shadows and darkness",15,28,True)
Diamond = Item("Diamond",80,"A Shiny Clear Gem. A Giant Covalent Structure Of Carbon Atoms You Believe.","Gemstone")
Topaz = Item("Topaz",30,"A Yellow Gem. Worth Lots To Any Merchant In The Trade.","Gemstone")
SouthernLootRoom.link_npc(ShadowMonster,"shadow monster")
SouthernLootRoom.link_item(Diamond,"diamond")
SouthernLootRoom.link_item(Topaz,"topaz")

#Kymar city
NorthKymar = Location("North Kymar", "North Kymar is the residential area. Most citizens have houses here but there is very little trade or work.")
Citizen2 = NPC("Citizen","A citizen leaving their house. Probably on their way to work")
Citizen2.addline("Haven’t got the time to talk I’m afraid")
KymarGuard2 = NPC("Kymar Guard","He used to be an adventurer like you. Until he took an arrow to the knee.")
KymarGuard2.addline("Move Along")
NorthKymar.link_npc(Citizen2,"citizen")
NorthKymar.link_npc(KymarGuard2,"guard")

WestKymar = Location("West Kymar", "West Kymar connects directly to the flower plains, and, as such, is Kymar’s hub of trade and commerce.")
KymarGuard3 = NPC("Kymar Guard","Just a normal guard of Kymar City.")
KymarGuard3.addline("Move Along")
Tourist2 = NPC("Tourist","A tourist browsing a merchant’s products")
Tourist2.addline("They have so many items for sale here")
Notepad = Item("Notepad",2,"A basic notepad with leather cover and the pages held together with dried honeycomb.","Notepad")
Tourist2.additem(Notepad)
RichMerchant = Merchant("Rich Merchant","A merchant happy to sell you anything as long as you can afford it.")
OrcishDagger = Weapon("Orcish Dagger",140,"A Large Dagger Made In The Orcish Mountains. Not Designed For Precise Attacks.","Dagger","fixed",1,40)
DwarvenBattleaxe = Weapon("Dwarven Battle-Axe Of Flames",250,"An Enchanted Weapon Made By Ancient Dwarven Blacksmiths. Imbued With The Power Of Fire, This Battle-Axe Will Deal A Mighty Blow.","Battle-Axe","floating",2,50)
LesserPotion = Potion("Lesser Health Potion",10,"A Small Health Potion That Can Be Used To Heal Someone",10)
GreatPotion = Potion("Great Health Potion",25,"A Medium Sized Health Potion That Can Be Used To Heal Someone",30)
Trinket = Item("Shiny Trinket",100,	"A Silver Trinket That Is Completely Useless. Worth A Good Penny Though.","Trinket")
RichMerchant.additem(OrcishDagger)
RichMerchant.additem(DwarvenBattleaxe)
RichMerchant.additem(LesserPotion)
RichMerchant.additem(GreatPotion)
WestKymar.link_npc(KymarGuard3,"guard")
WestKymar.link_npc(Tourist2,"tourist")
WestKymar.link_npc(RichMerchant,"rich merchant")

SouthKymar = Location("South Kymar","South Kymar is farthest away from any visitors so is used as the centre of industry within the city. Lots of jobs are found here, as well as it being the source for lots of Kymar’s valuable exports.")
KymarGuard4 = NPC("Kymar Guard","Just a normal guard of Kymar City.")
KymarGuard4.addline("Move Along")
FactoryWorker = NPC("Factory Worker","A citizen currently working in the factory. Covered head to toe in grease, it looks like they haven’t showered in a while.")
FactoryWorker.addline("These products aren’t going to make themselves")
Wrench = Item("Wrench",5,"The Staple Tool Of Any Factory Worker","Tool")
FactoryWorker.additem(Wrench)
MachinePart = Item("Machine Part", 25, "A Part Of Some Sort Of Machine. Useless To You But Perhaps Worth Something To A Merchant.","Scrap")
SouthKymar.link_npc(KymarGuard4,"guard")
SouthKymar.link_npc(FactoryWorker,"factory worker")
SouthKymar.link_item(MachinePart,"piece of scrap")

WildPlains.link_location(LowerDistrict,"jonak city","the wild plains")
WildPlains.link_location(Corridor,"dragon claw dungeon","the wild plains")
WildPlains.link_location(FlowerPlains,"the flower plains","the wild plains")
LowerDistrict.link_location(CentreDistrict,"the center district","the lower district")
CentreDistrict.link_location(UpperDistrict,"the upper district","the center district")
FlowerPlains.link_location(GreatFoyer,"the deep pit dungeon","the flower plains")
FlowerPlains.link_location(WestKymar,"kymar city","the flower plains")
WestKymar.link_location(NorthKymar,"north kymar","west kymar")
NorthKymar.link_location(SouthKymar,"south kymar","north kymar")
SouthKymar.link_location(WestKymar,"west kymar","south kymar")
Corridor.link_location(WesternPassage,"the western passage","the corridor")
Corridor.link_location(EasternPassage,"the eastern passage","the corridor")
WesternPassage.link_location(WesternSideRoom,"the western side-room","the western passage")
EasternPassage.link_location(EasternSideRoom,"the eastern side-room","the eastern passage")
WesternPassage.link_location(GreatHall,"the great hall","the western passage")
GreatHall.link_location(BrokenBallroom,"the broken ballroom","the great hall")
BrokenBallroom.link_location(WindingStaircase,"the winding staircase","the broken ballroom")
WindingStaircase.link_location(DeepCellar,"the deep cellar","the winding staircase")
DeepCellar.link_location(WesternTreasureRoom,"the western treasure room","the deep cellar")
DeepCellar.link_location(EasternTreasureRoom,"the eastern treasure room","the deep cellar")
GreatFoyer.link_location(ElongatedCorridor,"the elongated corridor","the great foyer")
ElongatedCorridor.link_location(DarkSideRoom,"the dark sideroom","the elongated corridor")
ElongatedCorridor.link_location(RuinedTower,"the ruined tower","the elongated corridor")
ElongatedCorridor.link_location(DarkArena,"the dark arena","the elongated corridor")
ElongatedCorridor.link_location(ElvenPassageway,"the elven passageway","the elongated corridor")
ElvenPassageway.link_location(SouthernLootRoom,"the southern loot room","the elven passageway")
#========================================================================================================================

player  = Player() #Creates Player Object
player.move(LowerDistrict) #Puts Player In First Location
fists = Weapon("Bare Knuckles",0,"Your fists","Unarmed","conversion",2,4) #Creates The Starting Weapon "Fists"
player.equipedWeapon = fists #Sets Fists As The Equipped Weapon

def play(): #Creates Function So That Recursion Can Occur
    if player.health <= 0: #Checks If The Player Is Dead
        player.dead = True
    command = input("> ")
    commands = command.split(' ')
    if commands[0].lower() == "goto":
        if len(commands) > 1:
            argument = []
            for word in commands:
                if word != commands[0]:
                    argument.append(word)
            commands[1] = " ".join(map(str,argument))
            player.move(player.location.goto(commands[1]))
        else:
            type("Goto where?")
            play() #Commands For Moving To A New Location
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
            play() #Command For Talking To A NPC
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
            play() #Command For Outputting Inventory
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
            play() #Command For Stealing From A NPC
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
            type("Take what?") #Commands For Taking An Item From A Location
    elif commands[0].lower() == "fight":
        if len(commands) > 1:
            argument = []
            for word in commands:
                if word != commands[0]:
                    argument.append(word)
            commands[1] = " ".join(map(str,argument))
            if commands[1] in player.location.connectedNPCs:
                enemy = player.location.connectedNPCs[commands[1]]
                if isinstance(enemy,Enemy):
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
            play() #Command For Fighting A Non-Ambush Enemy
    elif commands[0].lower() == "equiped":
        type(player.equipedWeapon.get_name()+" is the currently equiped weapon.") #Command For Outputting Currently Equipped Weapon
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
            play() #Command For Equipping A Weapon
    elif commands[0].lower() == "sellto":
        if len(commands) > 1:
            argument = []
            for word in commands:
                if word != commands[0]:
                    argument.append(word)
            commands[1] = " ".join(map(str,argument)).title()
            if commands[1].lower() in player.location.connectedNPCs:
                npc = player.location.connectedNPCs[commands[1].lower()]
                if isinstance(npc,Merchant):
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
            play() #Command For Selling To A Merchant
    elif commands[0].lower() == "bal":
        type("You have "+str(player.cash)+"₿") #Command For Outputing The Player's Balance
    elif commands[0].lower() == "buyfrom":
        if len(commands) > 1:
            argument = []
            for word in commands:
                if word != commands[0]:
                    argument.append(word)
            commands[1] = " ".join(map(str,argument)).title()
            if commands[1].lower() in player.location.connectedNPCs:
                npc = player.location.connectedNPCs[commands[1].lower()]
                if isinstance(npc,Merchant):
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
            play() #Command For Buying Items From A Merchant
    elif commands[0].lower() == "drink":
        if len(commands) > 1:
            argument = []
            for word in commands:
                if word != commands[0]:
                    argument.append(word)
            argument = " ".join(map(str,argument)).title()
            if argument in player.inventory:
                item = player.inventory.pop(argument)
                if isinstance(item,Potion):
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
            type("Drink what?") #Command For Drinking A Potion
    elif commands[0].lower() == "health":
        type("You have "+str(player.health)+" health") #Command For Outputing Current Health
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
        type("health : view your current health") #Command For Outputting What Each Command Does
    else:
        type("I Don't Know How To Do That!")
        play()
    print()
type("Use help to view commands, By default answers are 8 bit")
print()
while not player.dead and not player.victorious: #Main Loop That Stops When The Player Is Dead Or Has Won
    player.location.info()
    defeated_ambushes = []
    for npc in player.location.connectedNPCs:
        if isinstance(player.location.connectedNPCs[npc],Enemy):
            if player.location.connectedNPCs[npc].ambush:
                type("You are attacked by "+player.location.connectedNPCs[npc].get_name()+" the "+npc) #Starts Fight If Ambushing Enemy Is In Location
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
                    break
                elif enemy.health <= 0:
                    type2("The enemy has been defeated!")
                    player.score += round((enemy.health+enemy.damage)/2)
                    defeated_ambushes.append(npc)
                    type("Your score is now "+str(player.score))
    for npc in defeated_ambushes:
        player.location.connectedNPCs.pop(npc)
    play() #Calls The Ability To Type Commands
name = username
try:
    file = open('scoreboard.csv','x') #Will create Scoreboard.csv if it doesn't already exist
    file.close()
except:
    pass
finally:
    scoreboard = []
    file = open('scoreboard.csv','r') #Reads The Scoreboard, Adds The Player's Score, Sorts It, And Outputs The Scores
    for line in file:
        line = line.split(',')
        line[1] = line[1].rstrip()
        scoreboard.append(line)
sorted = []
scoreboard.append([name,str(player.score)])
while len(scoreboard) > 0: #Sorts The scoreboard By The Score Values
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
file = open('scoreboard.csv','w') #ReWrites The Scoreboard With The New Scores
for score in sorted:
    file.write(score[0]+","+score[1]+"\n")
file.close()
