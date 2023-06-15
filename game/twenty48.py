# twenty48.py
import time
class Twenty48:
    def __init__(self):
        self.score = 0
        self.board = [[0 for _ in range(4)] for _ in range(4)]

    def push(self, direction):
        for i in range(3):
            if direction == "Up":       
                for row in range(1,4):   
                    for tile in self.board[row]:
                        if tile == 0:
                            continue
                        elif tile == self.board[row - 1][self.board[row].index(tile)]:
                            self.board[row - 1][self.board[row].index(tile)] *= 2
                            self.board[row][self.board[row].index(tile)] = 0
                            #self.score += self.board[row - 1][self.board[row].index(tile)]
                        elif self.board[row - 1][self.board[row].index(tile)] == 0:
                            self.board[row - 1][self.board[row].index(tile)] = tile
                            self.board[row][self.board[row].index(tile)] = 0
            elif direction == "Down":
                for row in range(2, -1, -1):   
                    for tile in self.board[row]:
                        if tile == 0:
                            continue
                        elif tile == self.board[row + 1][self.board[row].index(tile)]:
                            self.board[row + 1][self.board[row].index(tile)] *= 2
                            self.board[row][self.board[row].index(tile)] = 0
                            #self.score += self.board[row + 1][self.board[row].index(tile)]
                        elif self.board[row + 1][self.board[row].index(tile)] == 0:
                            self.board[row + 1][self.board[row].index(tile)] = tile
                            self.board[row][self.board[row].index(tile)] = 0
            elif direction == "Left":
                for col in range(1,4):   
                    for tile in self.board:
                        if tile[col] == 0:
                            continue
                        elif tile[col] == tile[col - 1]:
                            tile[col - 1] *= 2
                            tile[col] = 0
                            #self.score += tile[col - 1]
                        elif tile[col - 1] == 0:
                            print(True)
                            tile[col - 1] = tile[col]
                            tile[col] = 0
            elif direction == "Right":
                for col in range(2, -1, -1):   
                    for tile in self.board:
                        if tile[col] == 0:
                            print(True)
                            continue
                        elif tile[col] == tile[col + 1]:
                            print(True)
                            tile[col + 1] *= 2
                            tile[col] = 0
                            #self.score += tile[col + 1]
                        elif tile[col + 1] == 0:
                            print(True)
                            tile[col + 1] = tile[col]
                            tile[col] = 0
        print(self.board)
        

    def setNumber(self, row, col, number):
        self.board[row][col] = number
    
    def getNumber(self, row, col):
        return self.board[row][col]
    
    def addRandom(self):
        pass

    def isFull(self):
        for row in self.board:
            for col in row:
                if col == 0:
                    return False
        return True



print(Twenty48().board)    