#Naughts And Crosses In The Python Console
#Adam Baker

#Imports time for the 'animated' victory effect
import time

#Class For The Game Grid
class Grid:
    #Runs when game = Grid() runs
    def __init__(self):
        #Defines What Locations Are X, O, or Empty
        self.squares = [[],[],["A1","A2","A3","B1","B2","B3","C1","C2","C3"]]
        #When True it's Xs Turn, when False it's Os turn
        self.turn = True
        #Variable For If Someone Has Won
        self.victory = None
        #Variable for first output line
        self.line1 = ""
    #Function for printing out the game board
    def output(self):
        for location in self.squares[0]: #Checks what's in square A1, and adds the right characters to line 1
            if location == "A1":
                self.line1 = (" X |")
        for location in self.squares[1]:
            if location == "A1":
                self.line1 = (" O |")
        for location in self.squares[2]:
            if location == "A1":
                self.line1 = ("   |")

        for location in self.squares[0]: #Checks what's in square B1, and adds the right characters to line 1
            if location == "B1":
                self.line1 += ("| X |")
        for location in self.squares[1]:
            if location == "B1":
                self.line1 += ("| O |")
        for location in self.squares[2]:
            if location == "B1":
                self.line1 +=("|   |")

        for location in self.squares[0]: #Checks what's in square C1, and adds the right characters to line 1
            if location == "C1":
                self.line1 += ("| X ")
        for location in self.squares[1]:
            if location == "C1":
                self.line1 += ("| O ")
        for location in self.squares[2]:
            if location == "C1":
                self.line1 += ("|   ")

        for location in self.squares[0]: #Checks what's in square A2, and adds the right characters to line 2
            if location == "A2":
                self.line2 = (" X |")
        for location in self.squares[1]:
            if location == "A2":
                self.line2 = (" O |")
        for location in self.squares[2]:
            if location == "A2":
                self.line2 = ("   |")

        for location in self.squares[0]: #Checks what's in square B2, and adds the right characters to line 2
            if location == "B2":
                self.line2 += ("| X |")
        for location in self.squares[1]:
            if location == "B2":
                self.line2 += ("| O |")
        for location in self.squares[2]:
            if location == "B2":
                self.line2 +=("|   |")

        for location in self.squares[0]: #Checks what's in square C2, and adds the right characters to line 2
            if location == "C2":
                self.line2 += ("| X ")
        for location in self.squares[1]:
            if location == "C2":
                self.line2 += ("| O ")
        for location in self.squares[2]:
            if location == "C2":
                self.line2 += ("|   ")

        for location in self.squares[0]: #Checks what's in square A3, and adds the right characters to line 3
            if location == "A3":
                self.line3 = (" X |")
        for location in self.squares[1]:
            if location == "A3":
                self.line3 = (" O |")
        for location in self.squares[2]:
            if location == "A3":
                self.line3 = ("   |")

        for location in self.squares[0]: #Checks what's in square B3, and adds the right characters to line 3
            if location == "B3":
                self.line3 += ("| X |")
        for location in self.squares[1]:
            if location == "B3":
                self.line3 += ("| O |")
        for location in self.squares[2]:
            if location == "B3":
                self.line3 +=("|   |")

        for location in self.squares[0]: #Checks what's in square C3, and adds the right characters to line 3
            if location == "C3":
                self.line3 += ("| X ")
        for location in self.squares[1]:
            if location == "C3":
                self.line3 += ("| O ")
        for location in self.squares[2]:
            if location == "C3":
                self.line3 += ("|   ")

        print("   A    B    C") #Prints the game board out
        print("1",self.line1)
        print("  =============")
        print("2",self.line2)
        print("  =============")
        print("3",self.line3)
        print()
        if self.turn: #Prints out who's turn it is
            print("-----X-Turn-----")
        else:
            print("-----O-Turn-----")
    #Function for getting input from the user
    def input(self):
        badmove = False
        print()
        coord = input(">>> ")
        if coord.upper() != "A1" and coord.upper() != "A2" and coord.upper() != "A3" and coord.upper() != "B1" and coord.upper() != "B2" and coord.upper() != "B3" and coord.upper() != "C1" and coord.upper() != "C2" and coord.upper() != "C3":
            print("Please Input A Co-ordinate e.g B3") #Must Be A Valid Co-ord Input
            self.input()
        else:
            if self.turn:
                for location in self.squares[1]:
                    if location == coord.upper(): #Stops Player From Replacing Used Square
                        print("That square has already been used")
                        badmove = True
                        self.input()
                for location in self.squares[0]:
                    if location == coord.upper(): #Stops Player From Replacing Used Square
                        print("That square has already been used")
                        badmove = True
                        self.input()
                if not badmove: #Continues If Move Is Allowed
                    self.squares[2].remove(coord.upper())
                    self.squares[0].append(coord.upper()) #Moves Co-ord from Empty to X
                    self.turn = False #Makes it O's turn
                    print()
            else:
                for location in self.squares[0]:
                    if location == coord.upper(): #Stops Player From Replacing Used Square
                        print("That square has already been used")
                        badmove = True
                        self.input()
                    for location in self.squares[1]:
                        if location == coord.upper(): #Stops Player From Replacing Used Square
                            print("That square has already been used")
                            badmove = True
                            self.input()
                if not badmove: #Continues If Move Is Allowed
                    self.squares[2].remove(coord.upper())
                    self.squares[1].append(coord.upper()) #Moves Co-ord from Empty to O
                    self.turn = True #Makes it X's Turn
                    print()
    #Function for checking if game has been won
    def winstate(self):
        #Has X won?
        if ("A1" in self.squares[0] and "A2" in self.squares[0] and "A3" in self.squares[0]) or ( "B1" in self.squares[0] and "B2" in self.squares[0] and "B3" in self.squares[0]) or ( "C1" in self.squares[0] and "C2" in self.squares[0] and "C3" in self.squares[0]) or ( "A1" in self.squares[0] and "B1" in self.squares[0] and "C1" in self.squares[0]) or ( "A2" in self.squares[0] and "B2" in self.squares[0] and "C2" in self.squares[0]) or ( "A3" in self.squares[0] and "B3" in self.squares[0] and "C3" in self.squares[0]) or ("A1" in self.squares[0] and "B2" in self.squares[0] and "B3" in self.squares[0]) or ("A3" in self.squares[0] and "B2" in self.squares[0] and "C1" in self.squares[0]):
            self.victory = "X"
        #Has O won?
        elif ("A1" in self.squares[1] and "A2" in self.squares[1] and "A3" in self.squares[1]) or ( "B1" in self.squares[1] and "B2" in self.squares[1] and "B3" in self.squares[1]) or ( "C1" in self.squares[1] and "C2" in self.squares[1] and "C3" in self.squares[1]) or ( "A1" in self.squares[1] and "B1" in self.squares[1] and "C1" in self.squares[1]) or ( "A2" in self.squares[1] and "B2" in self.squares[1] and "C2" in self.squares[1]) or ( "A3" in self.squares[1] and "B3" in self.squares[1] and "C3" in self.squares[1]) or ("A1" in self.squares[1] and "B2" in self.squares[1] and "B3" in self.squares[1]) or ("A3" in self.squares[1] and "B2" in self.squares[1] and "C1" in self.squares[1]):
            self.victory = "O"
        else:
            #Is the board full?
            if len(self.squares[2]) == 0:
                self.victory = "Draw"

game = Grid() #Assigns variable to class
while game.victory == None: #Main loop, will stop when someone wins/it's a draw
    game.output() #Outputs the board
    game.input() #Asks for input
    game.winstate() #Checks if anyone has won
if game.victory == "X": #When X wins
    for i in range (50):
        print("X Wins")
        time.sleep(0.1)
elif game.victory == "O": #When O wins
    for i in range (50):
        print("O Wins")
        time.sleep(0.1)
elif game.victory == "Draw": #When it's a draw
    for i in range (50):
        print("It's A Draw")
        time.sleep(0.1)
