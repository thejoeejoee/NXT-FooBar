from __future__ import print_function
from Crypto.Random.random import randint
from PyPacMan.Block import Block
from PyPacMan.Grid import Grid
from PyPacMan.Point import Point

from PyPacMan.Robot import Robot
from PyPacMan.RobotHardware import RobotHardware
from PyPacMan.settings import SIDES, ROBOT_DEFAULT_START_POSITION, MAPS
from random import random
from math import floor

import wx
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
    r.sides_history.extend((2,))
    while not g.is_solved():
        #r.check_sides()
        #side = SIDES[int(floor(random()*4))]
        sides = r.get_sides_by_points([Grid.get_oposite_side(r.sides_history[-1])])
        side = sides[0][0]
        next_position = Grid.get_next_position(side, r._Robot__position)
        if not Grid.exists_position(next_position):
            continue
        if isinstance(g[next_position], Block):
            continue
        r.move(side)

lens = []
robot_hardware = RobotHardware()
for _ in range(50):
    g = Grid()
    for position in MAPS['default']:
        g[position] = Block

    r = Robot(g, robot_hardware)
    solve(r)
    moves = r.positions_history
    print(moves)
    lens.append(len(moves))
    r.positions_history = []

print(sum(lens)/float(len(lens)))


