from pathlib import Path
import re
import itertools

test_data = Path("test-data.txt").read_text().splitlines()


def is_vertical(x1, x2):
    return x1 == x2


def is_horizontal(y1, y2):
    return y1 == y2


def is_diagonal(x1, y1, x2, y2):
    return abs(x1 - x2) == abs(y1 - y2)


def get_range(val_1, val_2):
    start = min(val_1, val_2)
    end = max(val_1, val_2)
    return range(start, end + 1)


def get_diagonal_ranges(x1, y1, x2, y2):
    start, end = ((x1, y1), (x2, y2)) if x1 <= x2 else ((x2, y2), (x1, y1))

    x_line = range(start[0], end[0] + 1)
    y_direction = -1 if start[1] > end[1] else 1
    y_line = range(start[1], end[1] + y_direction, y_direction)

    return x_line, y_line


field_size = 1000
line_matrix = [[0] * field_size for _ in range(field_size)]

splitter = re.compile(r" -> |,")
for line in test_data:
    x1, y1, x2, y2 = list(map(int, re.split(splitter, line)))
    if is_vertical(x1, x2):
        for y in get_range(y1, y2):
            line_matrix[y][x1] += 1
    elif is_horizontal(y1, y2):
        for x in get_range(x1, x2):
            line_matrix[y1][x] += 1
    elif is_diagonal(x1, y1, x2, y2):
        for x, y in zip(*get_diagonal_ranges(x1, y1, x2, y2)):
            line_matrix[y][x] += 1

result = sum(
    itertools.chain.from_iterable(
        (int(val >= 2) for val in column) for column in line_matrix
    )
)
print(f"{result=}")
