class Segment(object):
    """
    base abstract part of game grid
    """

    def __init__(self, x, y):
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.position = x, y
        self.__x = x
        self.__y = y

    def __str__(self):
        raise NotImplementedError


