from UnknownSegment import UnknownSegment
from Block import Block
from Point import Point

SEGMENT_WIDTH = 10


class Diretions():
    top = 0
    right = 1
    bottom = 2
    left = 3


DIRECTIONS = (
    Diretions.top,
    Diretions.right,
    Diretions.bottom,
    Diretions.left
)

GRID_SEGMENTS = (
    UnknownSegment,
    Block,
    Point
)