from PyPacMan.Segment import Segment


class Point(Segment):
    """

    """

    def __init__(self, x, y):
        super(Point, self).__init__(x, y)
        self.__collected = False

    def collect(self):
        self.__collected = True
        print('on {} colected!'.format(self.position))

    def is_collected(self):
        return self.__collected

    def __str__(self):
        return '[{}0{}]'.format(self._x, self._y)
