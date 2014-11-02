from __future__ import print_function
from Crypto.Random.random import randint
from PyPacMan.Block import Block
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
    while not g.is_solved():
        #r.check_sides()
        #side = SIDES[int(floor(random()*4))]

        exclude_sides = []
        for side in SIDES:
            position = Grid.get_next_position(side, r._Robot__position)
            if not Grid.exists_position(position):
                exclude_sides.append(side)
                continue
            segment = r._Robot__grid[position]
            if isinstance(segment, Block):
                exclude_sides.append(side)
                continue

        side = r.get_sides_by_points(exclude_sides)[0][0]
        print(r.get_sides_by_points(exclude_sides))
        print(r)

        next_position = Grid.get_next_position(side, r._Robot__position)
        if not Grid.exists_position(next_position):
            continue
        if isinstance(g[next_position], Block):
            continue
        r.move(side)
    moves = len(r.positions_history)
    r.positions_history = []
    return moves

lens = []
robot_hardware = RobotHardware()
for _ in range(1):
    g = Grid()
    g[1, 1] = g[1, 2] = g[2, 1] = g[4, 1] = g[6, 1] = g[7, 1] = g[7, 2] = g[3, 3] = g[5, 3] = g[1, 4] = g[3, 5] = g[5, 5] = g[7, 4] = Block
    r = Robot(g, robot_hardware)
    lens.append(solve(r))


print(lens)
print(sum(lens)/len(lens))

print('Blocked?')
print(r)
print(r.get_sides_by_points())