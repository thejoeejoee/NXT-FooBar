from PyPacMan.UnknownSegment import UnknownSegment
from PyPacMan.settings import GRID_DEFAULT_WIDTH, GRID_DEFAULT_HEIGHT, GRID_SEGMENTS


class Grid(object):
    """
    game grid controller
    """

    def __init__(self, width=GRID_DEFAULT_WIDTH, height=GRID_DEFAULT_HEIGHT):
        assert isinstance(width, int)
        assert isinstance(height, int)
        self.width = width
        self.height = height
        self.__grid = []
        for _x in range(width):
            column = []
            for _y in range(height):
                column.append(UnknownSegment(_x, _y))
            self.__grid.append(column)
        pass

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
    def exists_position(width, height, position):
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
