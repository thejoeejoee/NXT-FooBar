from PyPacMan.RobotHardware import RobotHardware
from PyPacMan.Grid import Grid
from PyPacMan.settings import SIDES, ROBOT_DEFAULT_START_POSITION, Sides
from PyPacMan.Block import Block
from PyPacMan.Point import Point
from PyPacMan.UnknownSegment import UnknownSegment


class Robot(object):
    def __init__(self, grid, robot_hardware, position=ROBOT_DEFAULT_START_POSITION):
        """
        :param grid: Grid
        :param robot_hardware RobotHardware
        :param x: int
        :param y: int
        """
        assert isinstance(grid, Grid)
        assert isinstance(robot_hardware, RobotHardware)
        self.__grid = grid
        self.__x = position[0]
        self.__y = position[1]
        self.__position = position
        self.__hardware = robot_hardware
        self.__last_direction = None
        self.sides_history = []
        #self.__mode = RobotModes.waiting
        self.positions_history = []
        self.positions_history.append(position)

    def check_sides(self):
        """
        tests, if robot has reason to sonic check the line
        """
        for side in SIDES:
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
                self.scan_line(side)

    def scan_line(self, side):
        """
        call hardware and set segments into grid
        :param side: int
        :param position: tuple
        """
        blocks = self.__hardware.get_count_of_empty_blocks(side)
        position = self.__position
        for _ in range(blocks):
            position = Grid.get_next_position(side, position)
            if not self.set_known_segment(position, Point):
                break
        end_position = Grid.get_next_position(side, position)
        self.set_known_segment(end_position, Block)

    def set_known_segment(self, position, segment_class):
        if Grid.exists_position(position):
            if isinstance(self.__grid[position], UnknownSegment):
                self.__grid[position] = segment_class
            else:
                # fuck it, hardware or grid lies
                print('On {} I want set {}, but here is {}.'.format(position, segment_class, type(self.__grid[position])))
            return True
        else:
            return False

    def get_sides_by_points(self, exclude_sides=[]):
        # try test another alg
        side_results = []
        include_sides = []
        sides = list(SIDES)
        #shuffle(sides)
        for side in sides:
            if side in exclude_sides:
                continue
            position = Grid.get_next_position(side, self.__position)
            if not Grid.exists_position(position):
                continue
            segment = self.__grid[position]
            if isinstance(segment, Block):
                continue
            include_sides.append(side)

        if len(include_sides) == 0:
            return [[Grid.get_oposite_side(self.sides_history[-1])]]

        for side in include_sides:
            segments = []
            if side == Sides.top:
                y = 0
                while y < self.__y:
                    segments.extend(self.__grid.get_row(y))
                    y += 1
            elif side == Sides.right:
                x = self.__x + 1
                while x < self.__grid.width:
                    segments.extend(self.__grid.get_column(x))
                    x += 1
            elif side == Sides.bottom:
                y = self.__y + 1
                while y < self.__grid.height:
                    segments.extend(self.__grid.get_row(y))
                    y += 1
            elif side == Sides.left:
                x = 0
                while x < self.__x:
                    segments.extend(self.__grid.get_column(x))
                    x += 1
            count_of_uncollected_points = len(filter(lambda segment: isinstance(segment, Point) and not segment.is_collected(), segments))
            count_of_blocks = len(filter(lambda segment: isinstance(segment, Block), segments))
            count_of_all_segments = len(segments)

            side_results.append((side, count_of_uncollected_points / float(count_of_all_segments)**2))

        return tuple(sorted(side_results, key=lambda item: item[1], reverse=True))

    def move(self, side, length=1):
        assert side in SIDES
        new_position = self.__position
        self.sides_history.append(side)
        for _ in range(length):
            new_position = Grid.get_next_position(side, new_position)
            assert Grid.exists_position(new_position)
            self.positions_history.append(new_position)
            self.__grid.collect(new_position)
        try:
            self.__hardware.move(side, length)
        except:
            pass

        self.__x, self.__y = self.__position = new_position
        self.__last_direction = Grid.normalize_side(side)

    def solve_closed_way(self, side):
        start_position = self.__position
        #self.__mode = RobotModes.in_closed_way
        position = Grid.get_next_position(side, self.__position)
        length = 0
        while Grid.exists_position(position) and not isinstance(self.__grid[position], Block):
            length += 1
            position = Grid.get_next_position(side, position)
        self.move(side, length)


    def __str__(self):
        ret_str = ''
        grid = self.__grid._Grid__grid
        for y in range(self.__grid.height):
            for x, column in enumerate(grid):
                if self.__x == x and self.__y == y:
                    ret_str += '[RRR]'
                else:
                    ret_str += str(column[y])
            ret_str += '\n'
        return ret_str
