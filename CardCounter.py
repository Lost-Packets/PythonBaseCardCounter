import PySimpleGUI as sg
import numpy as np

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
        #properties
        self.runningCount = 0
        self.trueCount = 0
        self.DefualtDeck = self.Cards
        self.low = self.Cards[0:8] + self.Cards[13:20] + self.Cards[26:33] + self.Cards[39:50]  
        self.high = self.Cards[8:13] + self.Cards[21:26] + self.Cards[34:39] + self.Cards[47:53]

        # 8 decks
        self.totalHigh = 200
        self.totalLow = 200
        self.total = 416

        # 6 decks
        self.totalHigh6 = 150
        self.totalLow6 = 150
        self.total6 = 312

        # 4 decks
        self.totalHigh4 = 100
        self.totalLow4 = 100
        self.total4 = 208

        # 2 decks
        self.totalHigh2 = 50
        self.totalLow2 = 50
        self.total2 = 104
        
    def assignment(self, card):
        for card in self.FinalDeck:
            if card == card:
                self.FinalDeck.pop()
                break;  

        if card in self.low:
            self.runningCount = self.runningCount + 1

        elif card in self.high:
            self.runningCount = self.runningCount - 1

        else:
            self.runningCount = self.runningCount + 0
        
        self.countingStats(card)
 
    def TrueCount(self):
        self.trueCount = self.runningCount / round(len(self.FinalDeck) / 52)
        print("True Count : {}".format(self.trueCount))
        print("Deck Count : {}".format(len(self.FinalDeck)))

    def RunningCOunt(self):
        print("Running Count : {}".format(self.runningCount))

    def countingStats(self, card):
        if self.deckCount == 8:
            if card in self.high:
                self.totalHigh = self.totalHigh - 1
                self.total = self.total - 1
            elif card in self.low:
                self.totalLow = self.totalLow - 1
                self.total = self.total - 1
            print("% Of Next Card Being High: ", round(((self.totalLow / self.total)*100), 2), "%" )
            print("% Of Next Card Being Low: ", round(((self.totalHigh / self.total)*100), 2), "%" )

        elif self.deckCount == 6:
            if card in self.high:
                self.totalHigh6 = self.totalHigh6 - 1
                self.total6 = self.total6 - 1
            elif card in self.low:
                self.totalLow6 = self.totalLow6 - 1
                self.total6 = self.total6 - 1
            print("% Of Next Card Being High: ", round(((self.totalLow6 / self.total6)*100), 2), "%" )
            print("% Of Next Card Being Low: ", round(((self.totalHigh6 / self.total6)*100), 2), "%" )

        elif self.deckCount == 4:
            if card in self.high:
                self.totalHigh4 = self.totalHigh4 - 1
                self.total4 = self.total4 - 1
            elif card in self.low:
                self.totalLow4 = self.totalLow4 - 1
                self.total4 = self.total4 - 1
            print("% Of Next Card Being High: ", round(((self.totalLow4 / self.total4)*100), 2), "%" )
            print("% Of Next Card Being Low: ", round(((self.totalHigh4 / self.total4)*100), 2), "%" )

        elif self.deckCount == 2:
            if card in self.high:
                self.totalHigh2 = self.totalHigh2 - 1
                self.total2 = self.total2 - 1
            elif card in self.low:
                self.totalLow2 = self.totalLow2 - 1
                self.total2 = self.total2 - 1
            print("% Of Next Card Being High: ", round(((self.totalLow2 / self.total2)*100), 2), "%" )
            print("% Of Next Card Being Low: ", round(((self.totalHigh2 / self.total2)*100), 2), "%" )
                
class Player:
    def __init__(self):
        pass

# Main Program Loop
counter = CountingLog(8)
counter.Merg()

HeartsCol = [
    [sg.Text("Hearts")],
    [sg.Button("1 Hearts", key='-1 Hearts-')],
    [sg.Button("2 Hearts", key='-2 Hearts-')],
    [sg.Button("3 Hearts", key='-3 Hearts-')],
    [sg.Button("4 Hearts", key='-4 Hearts-')],
    [sg.Button("5 Hearts", key='-5 Hearts-')],
    [sg.Button("6 Hearts", key='-6 Hearts-')],
    [sg.Button("7 Hearts", key='-7 Hearts-')],
    [sg.Button("8 Hearts", key='-8 Hearts-')],
    [sg.Button("9 Hearts", key='-9 Hearts-')],
    [sg.Button("10 Hearts", key='-10 Hearts-')],
    [sg.Button("Ace Hearts", key='-Ace Hearts-')],
    [sg.Button("Jack Hearts", key='-Jack Hearts-')],
    [sg.Button("King Hearts", key='-King Hearts-')],
    [sg.Button("Queen Hearts", key='-Queen Hearts-')]
]

ClubsCol = [
    [sg.Text("Clubs")],
    [sg.Button("1 Clubs", key='-1 Clubs-')],
    [sg.Button("2 Clubs", key='-2 Clubs-')],
    [sg.Button("3 Clubs", key='-3 Clubs-')],
    [sg.Button("4 Clubs", key='-4 Clubs-')],
    [sg.Button("5 Clubs", key='-5 Clubs-')],
    [sg.Button("6 Clubs", key='-6 Clubs-')],
    [sg.Button("7 Clubs", key='-7 Clubs-')],
    [sg.Button("8 Clubs", key='-8 Clubs-')],
    [sg.Button("9 Clubs", key='-9 Clubs-')],
    [sg.Button("10 Clubs", key='-10 Clubs-')],
    [sg.Button("Ace Clubs", key='-Ace Clubs-')],
    [sg.Button("Jack Clubs", key='-Jack Clubs-')],
    [sg.Button("King Clubs", key='-King Clubs-')],
    [sg.Button("Queen Clubs", key='-Queen Clubs-')],
]

DiamondsCol = [
    [sg.Text("Diamonds", key='-OUTPUT-')],
    [sg.Button("1 Diamonds", key='-1 Diamonds-')],
    [sg.Button("2 Diamonds", key='-2 Diamonds-')],
    [sg.Button("3 Diamonds", key='-3 Diamonds-')],
    [sg.Button("4 Diamonds", key='-4 Diamonds-')],
    [sg.Button("5 Diamonds", key='-5 Diamonds-')],
    [sg.Button("6 Diamonds", key='-6 Diamonds-')],
    [sg.Button("7 Diamonds", key='-7 Diamonds-')],
    [sg.Button("8 Diamonds", key='-8 Diamonds-')],
    [sg.Button("9 Diamonds", key='-9 Diamonds-')],
    [sg.Button("10 Diamonds", key='-10 Diamonds-')],
    [sg.Button("Ace Diamonds", key='-Ace Diamonds-')],
    [sg.Button("Jack Diamonds", key='-Jack Diamonds-')],
    [sg.Button("King Diamonds", key='-King Diamonds-')],
    [sg.Button("Queen Diamonds", key='-Queen Diamonds-')],
]

SpadesCol = [
    [sg.Text("Spades")],
    [sg.Button("1 Spades", key='-1 Spades-')],
    [sg.Button("2 Spades", key='-2 Spades-')],
    [sg.Button("3 Spades", key='-3 Spades-')],
    [sg.Button("4 Spades", key='-4 Spades-')],
    [sg.Button("5 Spades", key='-5 Spades-')],
    [sg.Button("6 Spades", key='-6 Spades-')],
    [sg.Button("7 Spades", key='-7 Spades-')],
    [sg.Button("8 Spades", key='-8 Spades-')],
    [sg.Button("9 Spades", key='-9 Spades-')],
    [sg.Button("10 Spades", key='-10 Spades-')],
    [sg.Button("Ace Spades", key='-Ace Spades-')],
    [sg.Button("Jack Spades", key='-Jack Spades-')],
    [sg.Button("King Spades", key='-King Spades-')],
    [sg.Button("Queen Spades", key='-Queen Spades-')],
]

CardStat =[ [sg.Text('Card Statistics:')],
            [sg.Output(size=(70,15), key='-OUTPUT-')],]

layout = [[sg.Col(HeartsCol), sg.Col(ClubsCol), sg.Col(DiamondsCol), sg.Col(SpadesCol), sg.Col(CardStat)]]

sg.theme('DarkBlue')
window = sg.Window("demo", layout)
while True:
    #read window
    event, values = window.read()
    # Close window
    if event == sg.WIN_CLOSED:
        break
window.close()
