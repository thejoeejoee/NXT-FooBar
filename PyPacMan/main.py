from __future__ import print_function

from PyPacMan.Block import Block
from PyPacMan.Grid import Grid
from PyPacMan.Point import Point
from PyPacMan.Robot import Robot
from PyPacMan.RobotHardware import RobotHardware
from PyPacMan.settings import MAPS, SIDES, Sides, ROBOT_OPTIONS, random_map


"""
DIMENSIONS
0 - top
1 - right
2 - bottom
3 - left
"""


def print_moves_for_lua(r):
    for side, count in r.sides_history:
        if side in (Sides.bottom, Sides.left):
            side -= 2
        else:
            side += 2
        print('r:move({}, {})'.format(side, count))


def solve(r, g):
    r.set_known_segment((r.x, r.y), Block)
    r.move(Sides.top)

    print(r)
    raw_input()
    while not g.is_solved():
        # r.check_sides()
        # side = SIDES[int(floor(random()*4))]
        sides = r.get_sides_by_points(
            [Grid.get_oposite_side(r.sides_history[-1][0])])
        choosed_side = sides[0][0]
        for side in SIDES:
            next_position = Grid.get_next_position(side, r.position)
            if not Grid.exists_position(next_position):
                continue
            if isinstance(g[next_position], Block):
                continue
            if isinstance(g[next_position], Point) and not g[next_position].is_collected() and ROBOT_OPTIONS[
                'prefer_uncollected_point']:
                choosed_side = side

        for side in SIDES:
            if r.is_closed_way(side, r.position):
                choosed_side = side

        next_position = Grid.get_next_position(choosed_side, r.position)
        assert Grid.exists_position(next_position)
        assert not isinstance(g[next_position], Block)
        r.move(choosed_side)
        print(r)
        #print(sum(g.lengths_from_last_point)/len(g.lengths_from_last_point))


lens = []
robot_hardware = RobotHardware()
for _ in range(1):
    g = Grid()
    for position in random_map():
        g[position] = Block
    r = Robot(g, robot_hardware)
    solve(r, g)
    moves = r.positions_history
    # pprint(moves)
    # lens.append(len(moves))
    # lens.append(g.collected)
    lens.append(r._Robot__hardware.direction_changes)
    r.positions_history = []
    print_moves_for_lua(r)

print(r)
print(sum(lens) / float(len(lens)))


