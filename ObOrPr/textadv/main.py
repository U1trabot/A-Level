from room import Room
from item import Item
from character import Enemy, Character, Friend

kitchen = Room("Kitchen")
kitchen.set_description("A dark and dirty room, with grime and muck everywhere")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with a long central wooden table layed out with moldy food on cracked plates")

ballroom = Room("Ballroom")
ballroom.set_description("A large hall with a marbel floor, this hasn't been danced in for a millenia")

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')

starter_weapon = Item("Wooden Sword","A basic sword made out of cheap wood","Sword")

greg = Enemy("Greg", 'Just a normal dude')
greg.set_conversation("Hi, My name is greg, i'm just a normal dude trying to make his way in the text adventure")
greg.set_weakness("fork")
greg.set_item(starter_weapon)

greg_corpse = Character("Greg's Body", "The corpse of a perfectly innocent man that you just murdered")
greg_corpse.set_conversation("Nothing, because he's dead")

blob = Friend("Blob", "Just a blob of slime, kind of cute though")
blob.set_feeling(15)

dining_hall.set_character(greg)
ballroom.set_character(blob)
print()
current_room = kitchen
dead = False
while not dead:
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input(">>> ")
    if command in ["north","south","east","west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There is no-one to talk with")
    elif command == "fight":
        if inhabitant is not None:
            weapon = input("What will you fight with? ")
            if inhabitant.fight(weapon) == False:
                dead = True
            else:
                current_room.set_character(greg_corpse)
        else:
            print("There is no-one to fight with")
    elif command == "steal":
        if inhabitant is not None:
            inhabitant.steal()
        else:
            print("There is no-one to steal from")
    elif command == "hug":
        if inhabitant is not None:
            inhabitant.hug()
        else:
            print("There is no-one here to hug")

    print('\n')
print("Game Over")