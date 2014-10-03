from random import uniform, randint

from settings import SEGMENT_WIDTH, SONIC_SENSOR_INACCURACY


class RobotHardware(object):
    def get_count_of_empty_blocks(self, side):
        # ##### SOME HARDWARE MAGIC ABOUT SENSORS #####
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
            raise BrokenPipeError
        return int(blocks)