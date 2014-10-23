from PyPacMan.Block import Block
from PyPacMan.Point import Point
from PyPacMan.UnknownSegment import UnknownSegment

SEGMENT_WIDTH = 10
SONIC_SENSOR_INACCURACY = 3
MAX_GRID_RECURSIVE_DEPTH = 10
GRID_DEFAULT_WIDTH = 9
GRID_DEFAULT_HEIGHT = 6


class Diretions():
    top = 0
    right = 1
    bottom = 2
    left = 3


DIRECTIONS = (
    Diretions.top,
    Diretions.right,
    Diretions.bottom,
    Diretions.left,
)

DIRECTIONS_NAMES = (
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