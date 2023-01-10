from .fall_prevention_mode import *
import random

class PredMode(Mode):
    def __init__(self, verbose: bool = True):
        super().__init__(verbose)
        self.last_pred = random.randint(0,4)

    def collect(self, data: str):
        # parse vector from string
        # call prepare([vector]) (one item list)
        # call model
        # update last_pred
        self.last_pred = random.randint(0,4)
        return False

if __name__ == '__main__':
    print("Fall Prevention Predict Modes")