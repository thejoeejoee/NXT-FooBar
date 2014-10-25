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
grid[3, 0] = Block
grid[1, 1] = Block
grid[4, 1] = Block
grid[7, 1] = Block
grid[1, 2] = Block
grid[6, 2] = Block
grid[0, 3] = Block
grid[6, 3] = Block
grid[8, 4] = Block
grid[0, 5] = Block
grid[5, 5] = Block

r = Robot(grid, robot_hardware, 0, 0)

x = r.solve_closed_way(source_position=None, source_side=1)
print('Blocked?')
print(x)
print(r)


