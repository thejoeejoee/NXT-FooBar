from PyPacMan.Segment import Segment


class Point(Segment):
    """

    """

    def __init__(self, x, y):
        super(Point, self).__init__(x, y)
        self.__collected = False

    def collect(self, order):
        self.__collected = True
        self.__colected_order = order
        # print('on {} colected!'.format(self.position))

    def is_collected(self):
        return self.__collected

    def __str__(self):
        if self.__collected:
            return '[{:3}]'.format(self.__colected_order)
        else:
            return '[---]'
