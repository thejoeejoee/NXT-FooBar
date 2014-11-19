from random import randint

from PyPacMan.Block import Block
from PyPacMan.Point import Point
from PyPacMan.UnknownSegment import UnknownSegment


SEGMENT_WIDTH = 10
SONIC_SENSOR_INACCURACY = 3
GRID_MAX_RECURSIVE_DEPTH = 10
GRID_DEFAULT_WIDTH = 9
GRID_DEFAULT_HEIGHT = 6
GRID_START_BLOCKS = 2
GRID_BLOCKS = 11
GRID_EXTRA_START_BLOCK = 1

GRID_MAX_POINTS = GRID_DEFAULT_HEIGHT * GRID_DEFAULT_WIDTH - GRID_BLOCKS - GRID_START_BLOCKS - GRID_EXTRA_START_BLOCK

ROBOT_DEFAULT_START_POSITION = (4, 3)
ROBOT_OPTIONS = {
    'count_actually_line': False,
    'prefer_uncollected_point': True,
}

MAPS = {
    'default': (
        (1, 1), (1, 2), (2, 1), (4, 1), (6, 1), (7, 1), (7, 2), (3, 3), (5, 3), (1, 4), (3, 5), (5, 5), (7, 4)),
    'version1': (
        (0, 1), (1, 1), (2, 1), (1, 2), (3, 1), (3, 3), (5, 5), (5, 3), (3, 5), (7, 4), (6, 1), (7, 1), (7, 2)),
    'version2': (
        (2, 0), (6, 0), (1, 1), (3, 1), (5, 1), (7, 1), (0, 3), (3, 3), (5, 3), (8, 3), (1, 4), (7, 4), (4, 5)),
    'version3': (
        (1, 1), (1, 4), (2, 1), (3, 1), (3, 3), (2, 4), (4, 0), (5, 1), (5, 3), (6, 4), (6, 1), (7, 1), (7, 4)),
    'version4': (
        (0, 3), (1, 0), (2, 2), (2, 4), (3, 3), (4, 5), (4, 1), (5, 3), (4, 0), (6, 2), (6, 4), (7, 0), (8, 3)),
    'version5': (
        (1, 0), (1, 3), (2, 5), (3, 1), (3, 2), (3, 3), (7, 3), (4, 4), (5, 1), (5, 2), (5, 3), (6, 5), (7, 0)),
    'empty': (),
}


def random_map():
    positions = [(3, 3), (5, 3)]
    while len(positions) <= 13:
        x = randint(0, GRID_DEFAULT_WIDTH - 1)
        y = randint(0, GRID_DEFAULT_HEIGHT - 1)
        position = x, y
        if position == (4, 3):
            continue
        if position in positions:
            continue
        else:
            positions.append(position)
    return tuple(positions)


class Directions():
    horizont = 0
    vertical = 1


class Sides():
    top = 0
    right = 1
    bottom = 2
    left = 3


SIDES = (
    Sides.top,
    Sides.right,
    Sides.bottom,
    Sides.left,
)

SIDES_NAMES = (
    'top',
    'right',
    'bottom',
    'left',
)

GRID_SEGMENTS = (
    UnknownSegment,
    Block,
    Point,
)