from __future__ import print_function
from pprint import pprint
from random import randint

from UnknownSegment import UnknownSegment
from Point import Point
from Block import Block
from Grid import Grid
from Robot import Robot
from RobotHardware import RobotHardware
"""
DIMENSIONS
0 - top
1 - right
3 - bottom
4 - left
"""

grid = Grid(width=9, height=6)
robot_hardware = RobotHardware()
#grid[8, 4] = Block(8, 4)
#grid[7, 5] = Point(7, 5)
for _y in range(6):
    for _x in range(9):
        grid[_x, _y] = (UnknownSegment, )[randint(0, 0)](_x, _y)
r = Robot(grid, robot_hardware, 3, 2)
r.check_sides()
print(r)
