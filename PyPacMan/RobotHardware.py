from random import uniform, randint

from PyPacMan.Grid import Grid
from PyPacMan.settings import SEGMENT_WIDTH, SONIC_SENSOR_INACCURACY, Directions


class RobotHardware(object):
    def __init__(self, last_direction=Directions.vertical):
        super(RobotHardware, self).__init__()
        self.last_direction = last_direction

    def get_count_of_empty_blocks(self, side):
        # ##### SOME HARDWARE MAGIC ABOUT SENSORS AND SIDE #####
        blocks = randint(0, 4)
        length = float(blocks * SEGMENT_WIDTH) + uniform(-float(SONIC_SENSOR_INACCURACY),
                                                         float(SONIC_SENSOR_INACCURACY))
        # ##### SOME HARDWARE MAGIC #####

        # mathematics
        probably_blocks, offset = divmod(length, SEGMENT_WIDTH)
        if offset < SONIC_SENSOR_INACCURACY:
            blocks = probably_blocks
        elif offset > SEGMENT_WIDTH - SONIC_SENSOR_INACCURACY:
            blocks = probably_blocks + 1
        else:
            raise BrokenPipeError('Unknown data from ultrasonic sensor, value: {}.'.format(length))
        return int(blocks)

    def move(self, side, length):
        # #####################################
        # SOME HW MAGIC
        # #####################################
        if not Grid.normalize_side(side) == self.last_direction:
            self.change_direction(Grid.normalize_side(side))

        print('Move {} blocks to {} side.'.format(length, side))

    def change_direction(self, direction):
        # #####################################
        # SOME HW MAGIC
        # #####################################
        print('direction changed to {}'.format(direction))