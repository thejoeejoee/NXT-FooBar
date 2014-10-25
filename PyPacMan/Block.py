from Segment import Segment


class Block(Segment):
    """
    hard part of game grid
    """

    def __init__(self, x, y):
        super(Block, self).__init__(x, y)

    def __str__(self):
        return '[XXX]'#.format(self._x, self._y)