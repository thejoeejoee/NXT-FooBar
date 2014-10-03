from __future__ import print_function
from Block import Block

from Grid import Grid
from Point import Point
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

grid[6, 4] = Block
grid[7, 4] = Point

r = Robot(grid, robot_hardware, 4, 5)
r.check_sides()
print(r)
