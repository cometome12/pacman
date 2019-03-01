import unittest
from Grid import Grid
from Pacman import Pacman
from helper import *
from constants import *

class Test(unittest.TestCase):

    def test_changeDirection(self):
        # test change once
        pacman = Pacman(0,0,NORTH)
        pacman.changeDirection(LEFT)
        self.assertEqual(pacman.direction, WEST)
        pacman.changeDirection(RIGHT)
        pacman.changeDirection(RIGHT)
        pacman.changeDirection(RIGHT)
        pacman.changeDirection(RIGHT)
        pacman.changeDirection(RIGHT)
        # test go around a circle
        self.assertEqual(pacman.direction, NORTH)

    def test_move(self):
        # normal movement
        pacman = Pacman(0,0,NORTH)
        pacman.move()
        self.assertEqual(pacman.x, 0)
        self.assertEqual(pacman.y, 1)
        # move around
        pacman.move()
        pacman.move()
        pacman.changeDirection(RIGHT)
        pacman.move()
        pacman.move()
        self.assertEqual(pacman.x, 2)
        self.assertEqual(pacman.y, 3)

    def test_detectBoundary(self):
        # test 4 edge cases
        grid = Grid(5,5)
        pacman = Pacman(0,0,WEST)
        self.assertTrue(isMoveOutOfBoundary(grid,pacman))
        pacman = Pacman(0,5,NORTH)
        self.assertTrue(isMoveOutOfBoundary(grid,pacman))
        pacman = Pacman(5,3,EAST)
        self.assertTrue(isMoveOutOfBoundary(grid,pacman))
        pacman = Pacman(3,0,SOUTH)
        self.assertTrue(isMoveOutOfBoundary(grid,pacman))
        # test normal case
        pacman = Pacman(3,2,SOUTH)
        self.assertFalse(isMoveOutOfBoundary(grid,pacman))

    def test_validPlace(self):
        grid = Grid(5,5)
        # random commands
        command = 'PDFS SDFSD SDFSDF'
        self.assertFalse(isPlaceCommand(command))
        self.assertFalse(isValidDrection(command))
        self.assertFalse(isValidXY(command,grid))
        command = 'PLACE SDFSD'
        self.assertFalse(isPlaceCommand(command))
        self.assertFalse(isValidDrection(command))
        self.assertFalse(isValidXY(command,grid))
        # test place command format, direction and if is valid x,y
        command = 'PLACE 3,4,SDF'
        self.assertTrue(isPlaceCommand(command))
        self.assertFalse(isValidDrection(command))
        self.assertTrue(isValidXY(command,grid))
        command = 'PLACE 3,4,SOUTH'
        self.assertTrue(isPlaceCommand(command))
        self.assertTrue(isValidDrection(command))
        self.assertTrue(isValidXY(command,grid))
        command = 'PLACE 6,6,SOUTH'
        self.assertTrue(isPlaceCommand(command))
        self.assertTrue(isValidDrection(command))
        self.assertFalse(isValidXY(command,grid))

    def test_createPacmanFromCommand(self):
        # successful creation
        command = "PLACE 4,5,SOUTH"
        pacman = createPacmanFromCommand(command)
        self.assertEqual(pacman.x, 4)
        self.assertEqual(pacman.y, 5)
        self.assertEqual(pacman.direction, SOUTH)
        # not successful creation, return a default pacman
        command = 'PSDF DSFDSF'
        pacman = createPacmanFromCommand(command)
        self.assertEqual(pacman.x, 0)
        self.assertEqual(pacman.y, 0)
        self.assertEqual(pacman.direction, NORTH)


if __name__ == '__main__':
    unittest.main()
