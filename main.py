from __future__ import print_function
from pprint import pprint
from random import randint

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

grid[8, 3] = Block
grid[7, 5] = Point(7, 5)

r = Robot(grid, robot_hardware, 8, 5)
r.check_sides()
print(r)
