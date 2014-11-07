from __future__ import print_function

from PyPacMan.Block import Block
from PyPacMan.Grid import Grid
from PyPacMan.Robot import Robot
from PyPacMan.RobotHardware import RobotHardware
from PyPacMan.settings import MAPS


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

global l
l = []

def solve(r, g):
    r.sides_history.extend((2, 2,))
    while not g.is_solved():
        #r.check_sides()
        #side = SIDES[int(floor(random()*4))]
        sides = r.get_sides_by_points([Grid.get_oposite_side(r.sides_history[-1]), Grid.get_oposite_side(r.sides_history[-2])])
        choosed_side = sides[0][0]
        
        next_position = Grid.get_next_position(choosed_side, r._Robot__position)
        assert Grid.exists_position(next_position)
        assert not isinstance(g[next_position], Block)
        r.move(choosed_side)

    print(sum(g.lengths_from_last_point)/len(g.lengths_from_last_point))

lens = []
robot_hardware = RobotHardware()
for _ in range(50):
    g = Grid()
    for position in MAPS['default']:
        g[position] = Block
    r = Robot(g, robot_hardware)
    solve(r, g)
    moves = r.positions_history
    #pprint(moves)
    lens.append(len(moves))
    r.positions_history = []


print(sum(lens) / float(len(lens)))


