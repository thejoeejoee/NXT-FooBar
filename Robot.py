from UnknownSegment import UnknownSegment
from Grid import Grid


class Robot(object):
    # requiring x and y depends on robosoutez.cz
    def __init__(self, grid, robot_hardware, x=None, y=None):
        """
        :param grid: Grid
        :param robot_hardware RobotHardware
        :param x: int
        :param y: int
        """
        assert isinstance(grid, Grid)
        self.__grid = grid
        self.__x = x
        self.__y = y
        self.__hardware = robot_hardware

    def get_actual_row(self):
        return self.__grid.get_row(self.__y)

    def get_actual_column(self):
        return self.__grid.get_column(self.__x)

    def check_sides(self):
        flags = self.__get_edge_flags()
        for i, flag in enumerate(flags):
            next_position = self.__get_next_position(i, self.__x, self.__y)
            if not flag and isinstance(self.__grid[next_position], UnknownSegment):
                self.check_line(self.__grid[self.__x, self.__y], i)

    def check_line(self, start_segment, side):
        x, y = start_segment.position
        length = self.__hardware.get_length(side)

    @staticmethod
    def __get_next_position(side, *position):
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

    def __get_edge_flags(self):
        """
        check, if is robot on one of edge
        """
        flags = [False, False, False, False]
        if self.__y == 0:
            flags[0] = True
        elif self.__y == self.__grid.height - 1:
            flags[2] = True

        if self.__x == 0:
            flags[3] = True
        elif self.__x == self.__grid.width - 1:
            flags[1] = True
        return tuple(flags)


    def __str__(self):
        ret_str = ''
        grid = self.__grid.get_whole_grid()
        for y in range(self.__grid.height):
            for x, column in enumerate(grid):
                if self.__x == x and self.__y == y:
                    ret_str += '[RRR]'
                else:
                    ret_str += str(column[y])
            ret_str += '\n'
        return ret_str
