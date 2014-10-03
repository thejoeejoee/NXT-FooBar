from Block import Block
from RobotHardware import RobotHardware
from UnknownSegment import UnknownSegment
from Grid import Grid
from settings import DIRECTIONS


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
        assert isinstance(robot_hardware, RobotHardware)
        self.__grid = grid
        self.__x = x
        self.__y = y
        self.__position = x, y
        self.__hardware = robot_hardware

    def get_actual_row(self):
        return self.__grid.get_row(self.__y)

    def get_actual_column(self):
        return self.__grid.get_column(self.__x)

    def check_sides(self):
        for side in DIRECTIONS:
            scan_line = False
            next_position = Grid.get_next_position(side, self.__position)
            if not Grid.exists_position(self.__grid.width, self.__grid.height, next_position):
                continue
            while next_position[0] and next_position[1] and next_position[0] != self.__grid.width and next_position[
                1] != self.__grid.height:
                next_segment = self.__grid[next_position]
                if isinstance(next_segment, Block):
                    break
                if isinstance(next_segment, UnknownSegment):
                    scan_line = True
                next_position = Grid.get_next_position(side, next_position)
            if scan_line:
                self.scan_line(side, self.__x, self.__y)

    def scan_line(self, side, *position):
        assert isinstance(position, tuple) and len(position) == 2
        x, y = position
        length = self.__hardware.get_length(side)

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
