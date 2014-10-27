from PyPacMan.RobotHardware import RobotHardware
from PyPacMan.Grid import Grid
from PyPacMan.settings import DIRECTIONS, MAX_GRID_RECURSIVE_DEPTH
from PyPacMan.Block import Block
from PyPacMan.Point import Point
from PyPacMan.UnknownSegment import UnknownSegment


class Robot(object):
    def __init__(self, grid, robot_hardware, x=4, y=3):
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
        self.__last_direction = None

    def solve_closed_way(self, source_position, source_side):
        self.tested_position = []
        return self.is_closed_way(source_position, source_side)

    def is_closed_way(self, source_side, source_position, length=1):
        """
        some recursive magic about closed ways problem
        :return:
        """
        if source_position is None:
            source_position = self.__position
        if length > MAX_GRID_RECURSIVE_DEPTH:
            return False
        target_position = Grid.get_next_position(source_side, source_position)  # zjisti pozici, ze ktere bude testovat
        if not Grid.exists_position(target_position):
            return True

        if isinstance(self.__grid[target_position], Block):
            return True

        sides = list(DIRECTIONS)
        sides.remove(Grid.get_oposite_side(source_side))  # bez vstupni strany
        free_sides = []  # slovnik indexovany stranou oznacujici blokovany pozice
        for side in sides:
            position = Grid.get_next_position(side, target_position)
            if not Grid.exists_position(position):  # pokud pozice neexistuje, je blokovano
                continue
            if position in self.tested_position: # jiz byl testovan, nebudu testovat
                continue
            else:
                self.tested_position.append(position)

            segment = self.__grid[position]  # vytazeni vedlejsiho segmentu
            if isinstance(segment, (Point, UnknownSegment)):  # pokud to je block, je blokovany
                free_sides.append(side)
        if len(free_sides) == 0:  # pokud zadny volny, je blokovany
            return True
        blocked = []
        print('    '*(length-1)+'from {} is free {} - ({})'.format(target_position, free_sides, length))
        for side in free_sides:
            blocked.append(self.is_closed_way(source_position=target_position, source_side=side, length=length + 1))
        return all(blocked)


    def check_sides(self):
        """
        tests, if robot has reason to sonic check the line
        """
        for side in DIRECTIONS:
            scan_line = False
            next_position = Grid.get_next_position(side, self.__position)
            if not Grid.exists_position(next_position):
                continue
            while Grid.exists_position(next_position):
                next_segment = self.__grid[next_position]
                if isinstance(next_segment, Block):
                    break
                if isinstance(next_segment, UnknownSegment):
                    scan_line = True
                next_position = Grid.get_next_position(side, next_position)
            if scan_line:
                self.scan_line(side, self.__position)

    def scan_line(self, side, position):
        """
        call hardware and set segments into grid
        :param side: int
        :param position: tuple
        """
        assert isinstance(position, tuple) and len(position) == 2
        blocks = self.__hardware.get_count_of_empty_blocks(side)
        position = self.__position
        for _ in range(blocks):
            position = Grid.get_next_position(side, position)
            if not self.set_known_segment(position, Point):
                break
        end_position = Grid.get_next_position(side, position)
        self.set_known_segment(end_position, Block)

    def set_known_segment(self, position, segment_class):
        """
        :param position:
        :param segment_class:
        :return:
        """
        if Grid.exists_position(position):
            if isinstance(self.__grid[position], UnknownSegment):
                self.__grid[position] = segment_class
            else:
                # fuck it, hardware or grid lies
                print(
                    'On {} I want set {}, but here is {}.'.format(position, segment_class, type(self.__grid[position])))
            return True
        else:
            return False

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
