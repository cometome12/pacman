import re
from Pacman import Pacman
from Constants import *

def isPlaceCommand(command):
    # PLACE command regex
    placeRe = r'^PLACE\s\d{1},\d{1},\D+$'
    return re.match(placeRe, command)

def isValidDrection(command):
    inputs = command.split(' ')[1].split(',')
    return inputs[2] in [NORTH,SOUTH,EAST,WEST]

def isValidXY(command,grid):
    inputs = command.split(' ')[1].split(',')
    return int(inputs[0]) < grid.xLength and int(inputs[1]) < grid.yLength

def createPacmanFromCommand(command):
    inputs = command.split(' ')[1].split(',')
    return Pacman(int(inputs[0]),int(inputs[1]),inputs[2])

def isMoveOutOfBoundary(grid,pacman):
    exceedConditions = [
        pacman.direction == WEST and pacman.x == 0,
        pacman.direction == EAST and pacman.x == grid.xLength,
        pacman.direction == SOUTH and pacman.y == 0,
        pacman.direction == NORTH  and pacman.y == grid.yLength
    ]
    return any(exceedConditions)
