from PyPacMan.Segment import Segment


class Point(Segment):
    """

    """

    def __init__(self, x, y):
        super(Point, self).__init__(x, y)
        self.collected = False

    def __str__(self):
        return '[{}0{}]'.format(self._x, self._y)
