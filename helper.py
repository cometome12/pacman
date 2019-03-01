import re
from Pacman import Pacman
from constants import *

def isPlaceCommand(command):
    # PLACE command regex
    placeRe = r'^PLACE\s\d{1},\d{1},\D+$'
    return re.match(placeRe, command)

def transferCommand(command):
    # prevent the command passed in is not valid
    if not isPlaceCommand(command):
        return None
    return command.split(' ')[1].split(',')

def isValidDrection(command):
    inputs = transferCommand(command)
    return inputs[2] in [NORTH,SOUTH,EAST,WEST] if inputs else False

def isValidXY(command,grid):
    inputs = transferCommand(command)
    return int(inputs[0]) < grid.xLength and int(inputs[1]) < grid.yLength if inputs else False


def createPacmanFromCommand(command):
    inputs = transferCommand(command)
    # when command invalid, default Parman will be created to prevent further error
    return Pacman(int(inputs[0]),int(inputs[1]),inputs[2]) if inputs else Pacman(0,0,NORTH)

def isMoveOutOfBoundary(grid,pacman):
    exceedConditions = [
        pacman.direction == WEST and pacman.x == 0,
        pacman.direction == EAST and pacman.x == grid.xLength,
        pacman.direction == SOUTH and pacman.y == 0,
        pacman.direction == NORTH  and pacman.y == grid.yLength
    ]
    return any(exceedConditions)
