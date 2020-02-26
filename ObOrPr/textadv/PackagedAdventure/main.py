import rpg, time, sys

inventory = []

def type(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")
    sys.stdout.flush()

kitchen = rpg.Room("Kitchen")
kitchen.set_description("A dark and dirty room, with grime and muck everywhere")

dining_hall = rpg.Room("Dining Hall")
dining_hall.set_description("A large room with a long central wooden table layed out with moldy food on cracked plates")

ballroom = rpg.Room("Ballroom")
ballroom.set_description("A large hall with a marbel floor, this hasn't been danced in for a millenia")

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')

starter_weapon = rpg.Item("Wooden Sword","A basic sword made out of cheap wood","Sword")

greg = rpg.Enemy("Greg", 'Just a normal dude')
greg.set_conversation("Hi, My name is greg, i'm just a normal dude trying to make his way in the text adventure")
greg.set_weakness("Nintendo Switch")
greg.set_item(starter_weapon)

greg_corpse = rpg.Character("Greg's Body", "The corpse of a perfectly innocent man that you just murdered")
greg_corpse.set_conversation("Nothing, because he's dead")

switch = rpg.Item("Nintendo Switch", "An amazing portable video game console brought to you by Nintendo","Utility")

blob = rpg.Friend("Blob", "Just a blob of slime, kind of cute though")
blob.set_feeling(15)

dining_hall.set_character(greg)
ballroom.set_character(blob)
ballroom.set_item(switch)

gauntlet = rpg.Item("Infinity Gauntlet", "A golden gaunlet that has UNLIMITED POWER","Gaunlet")
stormbreaker = rpg.Item("Stormbreaker","A large axe that is capable for aiming for the head","Two Handed")

thanos = rpg.Enemy("Thanos", 'A large purple guy with a golden gauntlet on his left hand, his chin looks funny')
thanos.set_conversation("You are not the only one cursed with knowledge")
thanos.set_weakness("Infinity Gauntlet")
thanos.set_item(gauntlet)

kitchen.set_character(thanos)
dining_hall.set_item(stormbreaker)

print()
current_room = kitchen
dead = False
won = 0
while not dead and won < 2:
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    item = current_room.get_item()
    if item is not None:
        item.show()
    command = input(">>> ")
    if command in ["north","south","east","west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            type("There is no-one to talk with")
    elif command == "fight":
        if inhabitant is not None:
            weapon = input("What will you fight with? ")
            owned = False
            for slot in inventory:
                if slot.get_name() == weapon:
                    owned = True
            if owned:
                if inhabitant.fight(weapon) == False:
                    dead = True
                else:
                    current_room.set_character(None)
                    won += 1
            else:
                type("You do not have that item!")
        else:
            type("There is no-one to fight with")
    elif command == "steal":
        if inhabitant is not None:
             if inhabitant.steal():
                 inventory.append(inhabitant.get_item())
                 inhabitant.set_item(None)
        else:
            type("There is no-one to steal from")
    elif command == "hug":
        if inhabitant is not None:
            inhabitant.hug()
        else:
            type("There is no-one here to hug")
    elif command == "take":
        if item is not None:
            inventory.append(item)
            type(("You take the"+" "+item.get_name()))
            current_room.set_item(None)
        else:
            type("There is nothing here to take")
    elif command == "inv":
        type("-------Inventory-------")
        for slot in inventory:
            type(slot.get_name())
        type("-----------------------")
    type('\n')
    if rpg.Enemy.enemies_defeated == 1:
        won = True
if dead:
    type("Game Over")
if won == 2:
    type("You win")