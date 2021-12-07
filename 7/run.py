import statistics
from pathlib import Path

test_data = sorted(list(map(int, Path("test-data.txt").read_text().split(","))))


median = int(statistics.median(test_data))
mean = statistics.mean(test_data)


def crab_sum(val, average):
    return sum(i for i in range(abs(val - average) + 1))


def calc(avg, test_data):
    return sum(crab_sum(val, avg) for val in test_data)


print(f"Part 1: {sum(abs(val - median) for val in test_data)}")
print(f"Part 2: {min(calc(avg_type(mean), test_data) for avg_type in (round, int))}")
