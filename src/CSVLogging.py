import csv
import os
import io
import logging
from logging import handlers

# CSVFormatter takes log enteries and formats them into a CSV format
class CSVFormatter(logging.Formatter):
   def __init__(self, fmt=None, datefmt=None, style="%", validate=True):
      super().__init__(fmt, datefmt, style, validate)

   def format(self, record):
      string_io = io.StringIO()
      writer = csv.writer(string_io)
      writer.writerow(record.msg)
      record.msg = string_io.getvalue().strip()
      return super().format(record)

# CSVTimedRotatingFileHandlerWithHeader writes a CSV header during each new file rotation
class CSVTimedRotatingFileHandlerWithHeader(handlers.TimedRotatingFileHandler):
   def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None, errors=None, header=None):
      super().__init__(filename, when, interval, backupCount, encoding, delay, utc, atTime, errors)
      self._header = header
      if (os.path.getsize(self.baseFilename) == 0):
         self._write_header()

   def doRollover(self):
      super().doRollover()
      self._write_header()

   def _write_header(self):
      if (self._header is not None):
         writer = csv.writer(self.stream)
         writer.writerow(self._header)

   def setHeader(self, header):
      self._header = header
