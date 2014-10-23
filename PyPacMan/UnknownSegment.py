from PyPacMan.Segment import Segment


class UnknownSegment(Segment):
    """
    base abstract part of game grid
    """

    def __str__(self):
        return '[{}-{}]'.format(self.__x, self.__y)


