from __future__ import print_function
from PyPacMan.Grid import Grid
from PyPacMan.Block import Block
from PyPacMan.Point import Point
from PyPacMan.Robot import Robot
from PyPacMan.RobotHardware import RobotHardware
from PyPacMan.settings import DIRECTIONS, Diretions, DIRECTIONS_NAMES

"""
DIMENSIONS
0 - top
1 - right
2 - bottom
3 - left
"""

grid = Grid()
robot_hardware = RobotHardware()
grid[1, 0] = Block
grid[1, 1] = Block
grid[1, 2] = Block
grid[1, 3] = Block
grid[1, 4] = Block

grid[0, 5] = Block

grid[0, 1] = Point
grid[0, 2] = Point
grid[0, 3] = Point
grid[0, 4] = Point

r = Robot(grid, robot_hardware, 0, 0)
print(r)


