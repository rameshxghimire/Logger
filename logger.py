#!/usr/bin/env python3
"""
Logger module to log stdout to an external file.
Usage:
    Import the logger :
    from logger import Logger

    invoke sys.stdout and assign Logger with filename as a parameter:
    sys.stdout = Logger("file.txt")
"""
# imports
import sys
import datetime


class Logger:
    """
    Writes stdout log to external log file.
    """
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    # Write custom messages to the external log file
    def write(self, message: str) -> str:
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
