from abc import ABC, abstractmethod
import pandas as pd
import time
import os

COLS = ["FFSR1", "FFSR2", "FFSR3", "FFSR4", "RFSR1", "RFSR2", "RFSR3", "RFSR4", "WS", "Label"]

# The ESP32 sends data vector each 200ms
# So the collection lengh will be:
# time_t = DF_TOTAL_SAMPLES * 200ms
# e.g. DF_TOTAL_SAMPLES = 64, t_time = 64 * 200ms = 12.8 secs
DF_TOTAL_SAMPLES = 64

Labels = {
    "LC": 0,  # Laying Center
    "LL": 1,  # Laying Left
    "LR": 2,  # Laying Right
    "AL": 3,  # Alarm Left
    "AR": 4,  # Alarm Right
}

class Mode(ABC):
    @abstractmethod
    def __init__(self, verbose: bool = True):
        self.verbose = verbose
        self.count = 0

    @abstractmethod
    def collect(self, data: str):
        pass

if __name__ == '__main__':
    print("Fall Prevention Mode")