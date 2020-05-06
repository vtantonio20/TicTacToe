
class Board():
    EMPTY_SPACE = "                  "
    def __init__(self):
        self.cells = ["_", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print("\n" + self.EMPTY_SPACE + " %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))
        print(self.EMPTY_SPACE + "-----------")
        print(self.EMPTY_SPACE + " %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print(self.EMPTY_SPACE + "-----------")
        print(self.EMPTY_SPACE + " %s | %s | %s \n" %(self.cells[1], self.cells[2], self.cells[3]))

    def showHelpBoard(self):
        help_bo = ["_", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        print("\n" + self.EMPTY_SPACE + " %s | %s | %s " %(help_bo[7], help_bo[8], help_bo[9]))
        print(self.EMPTY_SPACE + "-----------")
        print(self.EMPTY_SPACE + " %s | %s | %s " %(help_bo[4],help_bo[5], help_bo[6]))
        print(self.EMPTY_SPACE + "-----------")
        print(self.EMPTY_SPACE + " %s | %s | %s \n" %(help_bo[1], help_bo[2], help_bo[3]))

    def clearBoard(self):
        self.cells = ["_", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def addToBoard(self, player, pos):
        self.cells[pos] = str(player)

    def checkCellEmpty(self, pos):
        if self.cells[pos] == " ":
            return True
        else:
            return False
    def checkWinner(self, currPlayer):
        #horizontal victories
        if self.cells[1] == currPlayer and self.cells[2] == currPlayer and self.cells[3] == currPlayer:
            return True
        if self.cells[4] == currPlayer and self.cells[5] == currPlayer and self.cells[6] == currPlayer:
            return True
        if self.cells[7] == currPlayer and self.cells[8] == currPlayer and self.cells[9] == currPlayer:
            return True
        #Vertical victories
        if self.cells[1] == currPlayer and self.cells[4] == currPlayer and self.cells[7] == currPlayer:
            return True
        if self.cells[2] == currPlayer and self.cells[5] == currPlayer and self.cells[8] == currPlayer:
            return True
        if self.cells[3] == currPlayer and self.cells[6] == currPlayer and self.cells[9] == currPlayer:
            return True
        #Diagonal victories
        if self.cells[7] == currPlayer and self.cells[5] == currPlayer and self.cells[3] == currPlayer:
            return True
        if self.cells[1] == currPlayer and self.cells[5] == currPlayer and self.cells[9] == currPlayer:
            return True
        return False

    def checkTie(self):
        for i in self.cells:
            if i == " ":
                return False
        return True
#-------------------------------------------------------------------------------
#run first
def main():
    run = True
    while run:
        for x, element in enumerate(players):
            turnPlayed = False
            #if not run:
            #    break
            while turnPlayed == False:
                board.display()
                try:
                    inp = input("Type the position that Player %s wants to go: " %(element))
                    if str(inp).lower() == 'help':
                        board.showHelpBoard()
                        inp = input("\nThese numbers correspond with the positions on the board.\nPress any key to continue")
                    else:
                        #print(board.checkCellEmpty(int(inp)))
                        if board.checkCellEmpty(int(inp)):
                            board.addToBoard(element, int(inp))
                            turnPlayed = True
                        elif int(inp) == 0:
                            raise Exception
                        else:
                            if str(inp).lower == 'help':
                                inp = input("\nThat position has already been played!\nPress any key to continue")
                except:
                    inp = input("\nError! Please enter a number 1-9\nPress any key to continue")

                if board.checkWinner(element):
                    run = False
                    return element
                if board.checkTie():
                    run = False
                    return

game = True
board = Board()
inp = input("Welcome to the tictactoe game!\nType help to show the numbers of each position on the board.\nPress any key to play. ")
players = ["X", "O"]

while game:
    winner = main()
    if winner == players[0] or winner == players[1]:
        print("\nPlayer " + str(winner) + " won the game!!!")
    else:
        print("\nScratch! Its a tie Game!!!")

    board.display()
    inp = input("\nWould you like to continue playing? Type Y/N. ")
    if not(str(inp).lower() == "y"):
        game = False
        print("Thank you for Playing!")
    board.clearBoard()

#board.display()
