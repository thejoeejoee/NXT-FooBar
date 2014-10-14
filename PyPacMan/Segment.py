class Segment(object):
    """
    base abstract part of game grid
    """

    def __init__(self, x, y):
        self.position = x, y
        self.x = x
        self.y = y

    def __str__(self):
        raise NotImplementedError


