import librtd
import datetime
import logging
from CSVLogging import CSVTimedRotatingFileHandlerWithHeader, CSVFormatter
from sensors import SMS8ChannelRTDBoard, WaveshareAnalogDigitalConverter

# Define constants
NUMBER_OF_RTD_SENSORS = 8
PATH_TO_LOG_FILE = "/media/crcdj/Elements/RTD board Sequent Microsystems/logs/rtd_readings.csv"
LOG_HEADER = ("Timestamp", "RTD 01", "RTD 02", "RTD 03", "RTD 04", "RTD 05", "RTD 06", "RTD 07", "RTD 08")

def main() -> None:
   rtd_board0 = SMS8ChannelRTDBoard(0, decimals = 2)
   rtd_readings = rtd_board0.read_all()
   timestamp = [datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")]
   rtd_readings = [*timestamp, *rtd_readings]

   waveshare_adc_dac = WaveshareAnalogDigitalConverter()

   # Create logger
   logger = logging.getLogger("SensorLogger")
   logger.setLevel(logging.DEBUG)

   # Create rotating file handler
   handler = CSVTimedRotatingFileHandlerWithHeader(filename = PATH_TO_LOG_FILE, when = "midnight",  header = LOG_HEADER)
   handler.setLevel(logging.DEBUG)

   # Add formatter to file handler
   formatter = CSVFormatter("%(message)s")
   handler.setFormatter(formatter)

   # Add file handler to the logger
   logger.addHandler(handler)

   # Log the readings
   logger.info(rtd_readings)

if __name__ == "__main__":
   main()
