from __future__ import print_function

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
grid[6, 3] = Point
r = Robot(grid, robot_hardware, 4, 3)
r.check_sides()
print(r)
