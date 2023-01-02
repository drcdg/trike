from .Sensor import Sensor
import librtd
import datetime

NUMBER_OF_RTD_CHANNELS = 8

class SMS8ChannelRTDBoard(Sensor):
    def __init__(self, stack_position: int, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # The stack_position is the position of this board in the stack of other RTD boards.
        self.stack_position = stack_position

    def read(self, channel: int) -> float:
        reading = librtd.get(self.stack_position, channel)
        if (self.decimals > 0):
            return round(reading, self.decimals)

        return reading

    def read_all(self) -> tuple[float]:
        # Add 1 to NUMBER_OF_RTD_CHANNELS because range() isn't inclusive of the end number
        channel_readings = ( self.read(i) for i in range(1, NUMBER_OF_RTD_CHANNELS + 1) )
        return channel_readings
