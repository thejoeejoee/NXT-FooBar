from PyPacMan.Segment import Segment


class UnknownSegment(Segment):
    """
    base abstract part of game grid
    """

    def __init__(self, x, y):
        super(UnknownSegment, self).__init__(x, y)

    def __str__(self):
        return '[{}-{}]'.format(self._x, self._y)


