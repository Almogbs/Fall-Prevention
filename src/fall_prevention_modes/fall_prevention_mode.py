from abc import ABC, abstractmethod
import pandas as pd
import time
import os

COLS = ["FFSR1", "FFSR2", "FFSR3", "FFSR4", "RFSR1", "RFSR2", "RFSR3", "RFSR4", "WS", "Label"]

# The ESP32 sends data vector each 200ms
# So the rate of the data collection will be:
# DF_UPDATE_RATE * 200ms
# e.g. DF_UPDATE_RATE = 5, we will get new sample to the dataset each 1 sec.
DF_UPDATE_RATE = 5
DF_TOTAL_SAMPLES = 25

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