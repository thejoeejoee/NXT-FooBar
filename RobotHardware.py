from settings import DIRECTIONS_NAMES
class RobotHardware(object):
    def get_length(self, side):
        print('I want length from {} side'.format(DIRECTIONS_NAMES[side]))
        pass
        # rotate ultrasonic sensor and scan length

