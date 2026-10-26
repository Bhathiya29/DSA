class Player:
    def __init__(self,name, marker):
        self.name = name
        # the X or the 0
        self.marker = marker

class Board:
    def __init__(self, size):
        self.reset(size)
    

    def reset(self,size):
        self.board = [["" for x in range(size)].copy() for y in range(size)]
        self.rowCounts = {}
        self.colCounts = {}
        self.diagCounts = {}
        self.size = size

    def place(self, player, x,y):
        marker = player.marker
        # Base case, it has already been marked
        if self.board[y][x] !="":
            return ValueError
        
        else:
            self.board[y][x] = marker


            # The Rows
            self.rowCounts[y] = self.rowCounts.get(y,{})
            self.rowCounts[y][marker] = self.rowCounts[y].get(marker, 0)+1

            if self.rowCounts[y][marker] == self.size:
                return True
            
            # The Columns
            self.colCounts[y] = self.rowCounts.get(y,{})
            self.colCounts[y][marker] = self.rowCounts[y].get(marker,0) +1

            if self.colCounts[x][marker] == self.size:
                return True
            
            if x==y:
                self.diagCounts["forwards"] = self.diagCounts.get("forwards",{})
                self.diagCounts["forwards"][marker] = self.diagCounts["forwards"].get(marker, 0)+1

                if self.diagCounts["forwards"][marker] == self.size:
                    return True
                
            if x+y == self.size -1:
                self.diagCounts["backwards"] = self.diagCounts.get("backwards",{})
                self.diagCounts["backwards"][marker] = self.diagCounts["backwards"].get(marker,0)+1

                if self.diagCounts["backwards"][marker] == self.size:
                    return True
                
            return False

class Game:
    def __init__(self, player1, player2, board):
        self.board = board
        self.player2 = player1
        self.player2 = player2
    

    def playGame(self):
        currTurn = 1
        gameDone = False
        while not gameDone:
            currPlayer = self.player1 if currTurn%2 ==1 else self.player2

            x = int(input("Write x position of market"))
            y = int(input("Write y position of marker"))

            if self.board.place(currPlayer, x, y):
                gameDone = True
                print(f"{currPlayer.name} Wins!")
            else:
                currTurn +=1
    

max = Player("Max", "x")
joe = Player ("Joe", "o")
board = Board(3)
game = Game(max,joe,board)

game.playGame()

            

            



        

        