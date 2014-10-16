from __future__ import print_function
from PyPacMan.Grid import Grid
from PyPacMan.Block import Block
from PyPacMan.Robot import Robot
from PyPacMan.RobotHardware import RobotHardware

"""
DIMENSIONS
0 - top
1 - right
2 - bottom
3 - left
"""

grid = Grid()
robot_hardware = RobotHardware()
grid[3, 3] = Block
grid[5, 3] = Block
r = Robot(grid, robot_hardware, 4, 3)
r.check_sides()
print(r)


