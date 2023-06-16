# twenty48.py
from PyQt6.QtCore import QThread
import random

class Twenty48:
    def __init__(self):
        self.score = 0
        self.board = [[0 for _ in range(4)] for _ in range(4)]
        self.count = 0

    def push(self, direction):
        self.count = 0
        for i in range(3):
            if direction == "Up":       
                for row in range(1,4):   
                    for col in range(4):
                        if self.board[row][col] == 0:
                            self.count += 1
                            continue
                        elif self.board[row][col] == self.board[row - 1][col]:
                            self.board[row - 1][col] *= 2
                            self.board[row][col] = 0
                            self.score += self.board[row - 1][col]
                        elif self.board[row - 1][col] == 0:
                            self.board[row - 1][col] = self.board[row][col]
                            self.board[row][col] = 0
                        else:
                            self.count += 1
            elif direction == "Down":
                for row in range(2, -1, -1):   
                    for col in range(4):
                        if self.board[row][col] == 0:
                            self.count += 1
                            continue
                        elif self.board[row][col] == self.board[row + 1][col]:
                            self.board[row + 1][col] *= 2
                            self.board[row][col] = 0
                            self.score += self.board[row + 1][col]
                        elif self.board[row + 1][col] == 0:
                            self.board[row + 1][col] = self.board[row][col]
                            self.board[row][col] = 0
                        else:
                            self.count += 1
            elif direction == "Left":
                for col in range(1,4):   
                    for row in range(4):
                        if self.board[row][col] == 0:
                            self.count += 1
                            continue
                        elif self.board[row][col] == self.board[row][col - 1]:
                            self.board[row][col - 1] *= 2
                            self.board[row][col] = 0
                            self.score += self.board[row][col - 1]
                        elif self.board[row][col - 1] == 0:
                            self.board[row][col - 1] = self.board[row][col]
                            self.board[row][col] = 0  
                        else:
                            self.count += 1 
            elif direction == "Right":
                for col in range(2, -1, -1):   
                    for row in range(4):
                        if self.board[row][col] == 0:
                            self.count += 1
                            continue
                        elif self.board[row][col] == self.board[row][col + 1]:
                            self.board[row][col + 1] *= 2
                            self.board[row][col] = 0
                            self.score += self.board[row][col + 1]
                        elif self.board[row][col + 1] == 0:
                            self.board[row][col + 1] = self.board[row][col]
                            self.board[row][col] = 0    
                        else:
                            self.count += 1                        
        print(self.board)
        print(self.count)
    
    def addRandom(self):
        pass

    def isFull(self):
        for row in self.board:
            for col in row:
                if col == 0:
                    return False
        return True

    def setRandomIndex(self):
        random_x = random.randint(0,3)
        random_y = random.randint(0,3)
        if self.board[random_x][random_y] != 0:
            self.setRandomIndex()
        elif self.count != 36:
            self.board[random_x][random_y] = random.choice([2, 2, 4])


print(Twenty48().board)    