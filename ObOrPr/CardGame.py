#Adam Baker
#Card Game
import random

class Card:
    #__init__ command creates the object attributes for the Card (suit, val)
    #when the variable is init-ialised
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    def showCard(self):
        print("{} of {}".format(self.value, self.suit))
class Deck:

    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for s in ["Spades","Clubs","Diamonds","Hearts"]:
            for v in range(1,14):
                self.cards.append(Card(s,v))
    def show(self):
        for c in self.cards:
            c.showCard()
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,1)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
class Player:

    def __init__(self):
        pass
deck = Deck()

print("======")
deck.shuffle()
deck.show()