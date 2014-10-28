from __future__ import print_function
from PyPacMan.Grid import Grid
from PyPacMan.Block import Block
from PyPacMan.Point import Point
from PyPacMan.Robot import Robot
from PyPacMan.RobotHardware import RobotHardware

"""
DIMENSIONS
0 - top
1 - right
2 - bottom
3 - left
"""

g = Grid()
robot_hardware = RobotHardware()

# g[0, 0] = Point
#
# g[1, 0] = Block
# g[1, 1] = Block
# g[1, 2] = Block
# g[2, 3] = Block
# g[3, 4] = Block
# g[3, 5] = Block
# g[1, 5] = Block



r = Robot(g, robot_hardware, (0, 0))

print(r.is_closed_way(source_position=None, source_side=2))
r.solve_closed_way(2)

print('Blocked?')
print(r)
print(r.positions_history)


