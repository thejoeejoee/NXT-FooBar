from UnknownSegment import UnknownSegment


class Grid(object):
    """
    game grid controller
    """

    def __init__(self, width=9, height=6):
        self.width = width
        self.height = height
        self.__grid = [[UnknownSegment(x, y) for x in range(width)] for y in range(height)]

    def __getitem__(self, indexes):
        if isinstance(indexes, tuple) and len(indexes) == 2:
            return self.__grid[indexes[1]][indexes[0]]
        elif isinstance(indexes, int):
            return self.__grid[indexes]
        raise IndexError('Unknown index')

    def __setitem__(self, indexes, segment):
        if isinstance(indexes, tuple) and len(indexes) == 2:
            self.__grid[indexes[1]][indexes[0]] = segment
        else:
            raise IndexError('Unknown index')
        return self

    def get_column(self, x):
        column = []
        for each_row in self.__grid:
            column.append(each_row[x])
        return column


    def get_row(self, y):
        return self.__grid[y]

    def get_whole_grid(self):
        return self.__grid

