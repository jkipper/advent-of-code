from collections import deque
from pathlib import Path

test_data = Path("test-data.txt").read_text()
fish = map(int, test_data.split(","))

fish_counter = deque([0] * 9)

days = 256
for i in fish:
    fish_counter[i] += 1
for _ in range(days):
    fish_counter.rotate(-1)
    fish_counter[6] += fish_counter[-1]

print(sum(fish_counter))
