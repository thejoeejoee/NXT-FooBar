from Segment import Segment


class Point(Segment):
    """

    """

    def __init__(self, x, y, blocked_sides=tuple()):
        super(Point, self).__init__(x, y)
        self.collected = False
        self.blocked_sides = blocked_sides

    def is_accessible_from(self, side):
        return not side in self.blocked_sides

    def __str__(self):
        return '[000]'
