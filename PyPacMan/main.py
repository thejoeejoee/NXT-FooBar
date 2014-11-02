from __future__ import print_function
from Crypto.Random.random import randint
from PyPacMan.Grid import Grid
from PyPacMan.Point import Point
from PyPacMan.Robot import Robot
from PyPacMan.RobotHardware import RobotHardware
from PyPacMan.settings import SIDES
from random import random
from math import floor
"""
DIMENSIONS
0 - top
1 - right
2 - bottom
3 - left
"""

#print(r.is_closed_way(source_position=None, source_side=2))
#r.solve_closed_way(2)
#print(r)

def solve(r):
    tried = 0
    while not g.is_solved():
        #r.check_sides()
        side = SIDES[int(floor(random()*4))]
        next_position = Grid.get_next_position(side, r._Robot__position)
        if not Grid.exists_position(next_position):
            continue
        if isinstance(g[next_position], Block):
            continue
        if next_position in r.positions_history and not tried < 10:

            tried += 1
            continue
        tried = 0
        r.move(side)
    moves = len(r.positions_history)
    r.positions_history = []
    return moves


lens = []
robot_hardware = RobotHardware()
for _ in range(200):
    g = Grid()
    g[1, 1] = g[1, 2] = g[2, 1] = g[4, 1] = g[6, 1] = g[7, 1] = g[7, 2] = g[3, 3] = g[5, 3] = g[1, 4] = g[3, 5] = g[5, 5] = g[7, 4] = Block
    r = Robot(g, robot_hardware)
    lens.append(solve(r))


print(lens)
print(sum(lens)/len(lens))

#print('Blocked?')
#print(r)

print(r.get_sides_by_points())