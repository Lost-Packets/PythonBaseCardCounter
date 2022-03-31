
class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} {}".format(self.value, self.suit))

class Deck:
    def __init__(self, deckCount):
        #Lists
        self.Cards = []
        self.FinalDeck = []

        #Pre lists
        self.eightDeck = []
        self.sixDeck = []
        self.fourDeck = []
        self.twoDeck = []
        
        #Properties
        self.deckCount = deckCount
        self.build()

    def deckBuilder(self):
        if(self.deckCount == 8):
            for i in range(4):
                for val in range(len(self.Cards)):
                    self.eightDeck.append(self.Cards[val])
            print("Eight Decks = ", len(self.eightDeck))
            self.FinalDeck = self.eightDeck.copy()

        elif(self.deckCount == 6):
            for i in range(3):
                for val in range(len(self.Cards)):
                    self.sixDeck.append(self.Cards[val])
            print("Six Decks = ", len(self.sixDeck))
            self.FinalDeck = self.sixtDeck.copy()

        elif(self.deckCount == 4):
            for i in range(2):
                for val in range(len(self.Cards)):
                    self.fourDeck.append(self.Cards[val])
            print("Four Decks = ", len(self.fourDeck))
            self.FinalDeck = self.fourDeck.copy()

        elif(self.deckCount == 2):
            for i in range(1):
                for val in range(len(self.Cards)):
                    self.twoDeck.append(self.Cards[val])
            print("Two Decks = ", len(self.twoDeck))
            self.FinalDeck = self.twoDeck.copy()
        
    def build(self):
        for i in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(2,11):
                self.Cards.append(Card(i,v))
            for q in ["Jack", "King", "Queen", "Ace",]:
                self.Cards.append(Card(q,i))

    def Merg(self):
        self.build()
        self.deckBuilder()

    def show(self):
        for c in self.Cards:
            c.show()
            print("Index: ",self.Cards.index(c))

class CountingLog(Deck):
    def __init__(self, deckCount):
        super().__init__(deckCount)
        self.runningCount = 0
        self.trueCount = 0
        self.DefualtDeck = self.Cards
        
    def assignment(self, card):
        for card in self.FinalDeck:
            if card == card:
                self.FinalDeck.pop()
                break;

        low = self.Cards[0:8] + self.Cards[13:20] + self.Cards[26:33] + self.Cards[39:50]  
        high = self.Cards[8:13] + self.Cards[21:26] + self.Cards[34:39] + self.Cards[47:53]  

        if card in low:
            self.runningCount = self.runningCount + 1

        elif card in high:
            self.runningCount = self.runningCount - 1

        else:
            self.runningCount = self.runningCount + 0
 
    def TrueCount(self):
        self.trueCount = self.runningCount / round(len(self.FinalDeck) / 52)
        print("True Count : {}".format(self.trueCount))
        print("Deck Count : {}".format(len(self.FinalDeck)))

    def RunningCOunt(self):
        print("Running Count : {}".format(self.runningCount))

class Player:
    def __init__(self):
        pass

# Main Program Loop
counter = CountingLog(8)
counter.Merg()

while True:
    _input = input("Enter Card (Diamonds Jack, 10 Diamonds, Diamonds Ace): ")
    if _input == "q":
        break

    inputSep = _input.split(" ")
    card = Card(inputSep[0], inputSep[1])
    counter.assignment(card)
    counter.TrueCount()
    counter.RunningCOunt()
    del card

