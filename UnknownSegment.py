from Segment import Segment
class UnknownSegment(Segment):
    """
    base abstract part of game grid
    """
    def __init__(self, x, y):
        assert isinstance(x, int)
        assert isinstance(y, int)
        super(UnknownSegment, self).__init__(x, y)

    def __str__(self):
        return '[{}-{}]'.format(self.x, self.y)


