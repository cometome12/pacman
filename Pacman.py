from Constants import *

class Pacman:

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.directions = [NORTH,EAST,SOUTH,WEST]

    def changeDirection(self, change):
        currentIndex = self.directions.index(self.direction)
        index = None
        if change == RIGHT:
            index = (currentIndex + 1) % 4
        else:
            index = (currentIndex - 1) % 4
        self.direction = self.directions[index]

    def move(self):
        if self.direction == NORTH:
            self.y += 1
        elif self.direction == SOUTH:
            self.y -= 1
        elif self.direction == WEST:
            self.x -= 1
        elif self.direction == EAST:
            self.x += 1

    def report(self):
        print(self.x, self.y, self.direction)
