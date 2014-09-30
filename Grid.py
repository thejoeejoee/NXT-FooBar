from settings import GRID_SEGMENTS
from UnknownSegment import UnknownSegment


class Grid(object):
    """
    game grid controller
    """

    def __init__(self, width=9, height=6):
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

