from pathlib import Path
from collections import deque


class WindowParser:
    increases = 0

    def __init__(self, data, window_size):
        self.measurements = deque(maxlen=window_size)
        for i in range(window_size):
            self.measurements.appendleft(int(data.readline()))
            for i in range(len(self.measurements)):
                self.measurements[i] += 1

    def add_next(self, val):
        prev_sum = self.measurements.pop()
        self.measurements.appendleft(0)
        for i in range(len(self.measurements)):
            self.measurements[i] += val
        if self.measurements[-1] > prev_sum:
            self.increases += 1


with Path("test_data.txt").open() as data:
    parser = WindowParser(data, 3)
    while depth := data.readline():
        parser.add_next(int(depth))
    print(parser.increases)
