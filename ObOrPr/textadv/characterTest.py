from character import Enemy

greg = Enemy("Greg", 'Just a normal dude')
greg.set_conversation("Hi, My name is greg, i'm just a normal dude trying to make his way in the text adventure")
greg.set_weakness("fork")
fight_with = input("What will you fight with: ")
greg.fight(fight_with)