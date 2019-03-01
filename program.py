if __name__ == "__main__":
    from Grid import Grid
    from Pacman import Pacman
    from constants import *
    from helper import *
    import sys

    # Initilize Grid and pacman. Grid is fixed 5 x 5
    grid = Grid(5,5)
    pacman = None

    # Recieve and handle inputs from users
    while(True):
        # check if it is the first time input
        if pacman is None:
            args = sys.argv[1:]
            # validate first input
            command = ' '.join(map(str,args))
            if not isPlaceCommand(command):
                print(MSG_PLACE)
                exit()
            if not isValidDrection(command):
                print(MSG_DIRECTION)
                exit()
            if not isValidXY(command,grid):
                print(MSG_XY)
                exit()
            # initilize the pacman
            pacman = createPacmanFromCommand(command)
        else:
            # validate further inputs from users
            command = input(MSG_FURTHER_COMMAND)
            if command not in [MOVE,REPORT,LEFT,RIGHT] and not isPlaceCommand(command):
                print(MSG_NOT_VALID_INPUT)
            else:
                if command == MOVE:
                    if isMoveOutOfBoundary(grid,pacman):
                         continue
                    else:
                        pacman.move()
                elif command == REPORT:
                    pacman.report()
                elif command == LEFT:
                    pacman.changeDirection(LEFT)
                elif command == RIGHT:
                    pacman.changeDirection(RIGHT)
                elif isPlaceCommand(command):
                    if isValidDrection(command) and isValidXY(command,grid):
                        pacman = createPacmanFromCommand(command)
                    else:
                        print(MSG_NOT_VALID_INPUT)
