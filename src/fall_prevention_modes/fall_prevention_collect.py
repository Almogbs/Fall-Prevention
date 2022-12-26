from .fall_prevention_mode import *

class CollectMode(Mode):
    def __init__(self, verbose: bool = True, label: int = 0):
        super().__init__(verbose)
        self.data_file = f"data_{time.strftime(f'%H-%M-%S_%d-%m-%Y', time.gmtime())}_{label}.csv"
        self.df = pd.DataFrame(columns=COLS)
        self.stored = 0
        self.label = label

    def collect(self, data: str):
        self.count += 1

        if self.verbose:
            print(data + f" {self.label}")

        data = data.split(" ")[2: -1]
        data.append(self.label)
        self.df = self.df.append(pd.Series(data, index=COLS), ignore_index=True)

        try:
            if self.count % DF_UPDATE_RATE == 0:
                self.df.to_csv(self.data_file)
                self.stored += 1

        except ValueError:
            pass

        if self.stored == DF_TOTAL_SAMPLES:
            print(f"{DF_TOTAL_SAMPLES} samples written to {self.data_file}, quitting...")
            os._exit(0)


if __name__ == '__main__':
    print("Fall Prevention Collect Mode")