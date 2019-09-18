class PotionSeller:
  def response(self, speech):
      if speech == "Hello, Potion Seller, I am going into battle and I want your strongest potions.":
          return "My potions are too strong for you, traveler."
      elif speech == "Potion Seller, I tell you I am going into battle, and I want only your strongest potions.":
          return "You can't handle my potions. They're too strong for you."
      elif speech == "Potion Seller, listen to me; I want only your strongest potions.":
          return "My potions would kill you, traveler. You cannot handle my potions."
      elif speech == "Potion Seller, enough of these games. I'm going into battle and I need your strongest potions.":
          return "My strongest potions would kill you, traveler. You can't handle my strongest potions. You'd better go to a seller that sells weaker potions."
      elif speech == "Potion Seller, I'm telling you right now; I'm going into battle and I need only your strongest potions.":
          return "You don't know what you ask, traveler. My strongest potions will kill a dragon let alone a man. You need a seller that sells weaker potions, because my potions are too strong."
      elif speech == "Potion Seller, I'm telling you I need your strongest potions. I'm going into battle! I'm going to battle and I need your strongest potions!":
          return "You can't handle my strongest potions! No one can! My strongest potions are fit for a beast let alone a man."
      elif speech == "Potion Seller, what do I have to tell you to get your potions? Why won't you trust me with your strongest potions, Potion Seller? I need them if I'm to be successful in the battle!":
          return "I can't give you my strongest potions because my strongest potions are only for the strongest beings and you are of the weakest."
      elif speech == "Well then that's it, Potion Seller. I'll go elsewhere. I'll go elsewhere for my potions.":
          return "That's what you'd better do."
      elif speech == "I'll go elsewhere for my potions and I'll never come back!":
          return "Good. You're not welcome here! My potions are only for the strongest and you're clearly are not of the strongest you're clearly the weakest."
      elif speech == "You've had your say, Potion Seller but I'll have mine. You're a rascal, you're a rascal with no respect for knights. No respect for anything...except your potions!":
          return "Why respect knights...when my potions can do anything that you can..."
      return "Command Not Recognised"
seller = PotionSeller()
while True:
    print(seller.response(input()))