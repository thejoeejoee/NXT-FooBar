class Segment(object):
    """
    base abstract part of game grid
    """

    def __init__(self, x, y):
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.position = x, y
        self._x = x
        self._y = y

    def __str__(self):
        raise NotImplementedError


