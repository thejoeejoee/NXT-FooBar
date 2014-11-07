from PyPacMan.Block import Block
from PyPacMan.Point import Point
from PyPacMan.UnknownSegment import UnknownSegment

SEGMENT_WIDTH = 10
SONIC_SENSOR_INACCURACY = 3
GRID_MAX_RECURSIVE_DEPTH = 1
GRID_DEFAULT_WIDTH = 9
GRID_DEFAULT_HEIGHT = 6
GRID_START_BLOCKS = 2
GRID_BLOCKS = 11
GRID_MAX_POINTS = GRID_DEFAULT_HEIGHT * GRID_DEFAULT_WIDTH - GRID_START_BLOCKS - GRID_BLOCKS - 1
ROBOT_DEFAULT_START_POSITION = (4, 3)

MAPS = {
    'default': ((1, 1), (1, 2), (2, 1), (4, 1), (6, 1), (7, 1), (7, 2), (3, 3), (5, 3), (1, 4), (3, 5), (5, 5), (7, 4)),
    'version1': ((0, 1), (1, 1), (2, 1), (1, 2), (3, 1), (3, 3), (5, 5), (5, 3), (3, 5), (7, 4), (6, 1), (7, 1), (7, 2)),
    'version2': ((2, 0), (6, 0), (1, 1), (3, 1), (5, 1), (7, 1), (0, 3), (3, 3), (5, 3), (8, 3), (1, 4), (7, 4), (4, 5))
}


class RobotModes():
    waiting = 0
    in_closed_way = 1


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