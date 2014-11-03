from PyPacMan.Block import Block
from PyPacMan.Point import Point
from PyPacMan.UnknownSegment import UnknownSegment
from PyPacMan.settings import GRID_DEFAULT_WIDTH, GRID_DEFAULT_HEIGHT, GRID_SEGMENTS, SIDES, Sides, Directions, \
    GRID_MAX_POINTS


class Grid(object):
    """
    game grid controller
    """

    def __init__(self, width=GRID_DEFAULT_WIDTH, height=GRID_DEFAULT_HEIGHT):
        assert isinstance(width, int)
        assert isinstance(height, int)
        self.width = width
        self.height = height
        self.__grid = [[Point(_x, _y) for _y in range(height)] for _x in range(width)]
        self.__collected = 0
        self.__last_collected_position = (0, 0)

    def __getitem__(self, indexes):
        if isinstance(indexes, tuple) and len(indexes) == 2:
            return self.__grid[indexes[0]][indexes[1]]
        elif isinstance(indexes, int):
            return self.__grid[indexes]
        raise IndexError('Unknown index')

    def __setitem__(self, indexes, segment):
        if isinstance(indexes, tuple) and len(indexes) == 2:
            if isinstance(segment, GRID_SEGMENTS):
                self.__grid[indexes[0]][indexes[1]] = segment
            else:
                self.__grid[indexes[0]][indexes[1]] = segment(indexes[0], indexes[1])
        else:
            raise IndexError('Unknown index')
        return self

    def collect(self, position):
        assert isinstance(position, tuple) and len(position) == 2
        assert Grid.exists_position(position)
        if isinstance(self[position], Block):
            assert False, 'I want to {}, but it is Block'.format(position)
        elif isinstance(self[position], UnknownSegment):
            self[position] = Point
            #assert False, 'I want to {}, but it is UnknownSegment'.format(position).

        if isinstance(self[position], Point):
            if not self[position].is_collected():

                print((abs(self.__last_collected_position[0]-position[0])**2 + (abs(self.__last_collected_position[1]-position[1])**2))**0.5)
                self.__last_collected_position = position
                self[position].collect()
                self.__collected += 1
        else:
            raise Exception

    def is_solved(self):
        return self.__collected > GRID_MAX_POINTS

    def get_free_directions(self, position, unknown_segments=True):
        assert len(position) == 2
        free_directions = []
        for side in SIDES:
            side_position = Grid.get_next_position(side, position)
            if not Grid.exists_position(side_position):
                continue
            # on position is Point or Unknown segment with flag
            if isinstance(self[side_position], Point) or unknown_segments and isinstance(self[side_position],
                                                                                         UnknownSegment):
                free_directions.append(side)
                continue
        return tuple(free_directions)

    def get_column(self, x):
        return self.__grid[x]

    def get_row(self, y):
        row = []
        for each_column in self.__grid:
            row.append(each_column[y])
        return row

    def get_whole_grid(self):
        return self.__grid

    @staticmethod
    def exists_position(position, width=GRID_DEFAULT_WIDTH, height=GRID_DEFAULT_HEIGHT):
        assert len(position) == 2
        if position[0] < 0 or position[1] < 0:
            return False
        if position[0] > width - 1 or position[1] > height - 1:  # because it's indexed from zero
            return False
        return True

    @staticmethod
    def get_next_position(side, position):
        assert len(position) == 2
        if side == 0:
            return position[0], position[1] - 1
        elif side == 1:
            return position[0] + 1, position[1]
        elif side == 2:
            return position[0], position[1] + 1
        elif side == 3:
            return position[0] - 1, position[1]
        else:
            raise IndexError

    @staticmethod
    def get_oposite_side(side):
        assert side in SIDES
        if side in (Sides.top, Sides.right):
            return side + 2
        elif side in (Sides.bottom, Sides.left):
            return side - 2

    @staticmethod
    def normalize_side(side):
        assert side in SIDES
        if side in (Sides.left, Sides.right):
            return Directions.horizont
        elif side in (Sides.top, Sides.bottom):
            return Directions.vertical
