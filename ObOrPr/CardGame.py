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
                if v == (1):
                    value = "Ace"
                elif v == (11):
                    value = "Jack"
                elif v == (12):
                    value = "Queen"
                elif v == (13):
                    value = "King"
                else:
                    value = v
                self.cards.append(Card(s,value))
    def show(self):
        for c in self.cards:
            c.showCard()
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,1)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    def drawCard(self):
        return self.cards.pop()
class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    def showHand(self):
        for card in self.hand:
            card.showCard()
deck = Deck()


deck.shuffle()
elprimo = Player("El Primo")
for i in range(5):
    elprimo.draw(deck)
elprimo.showHand()