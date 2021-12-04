import operator
from pathlib import Path


data = Path("test-data.txt").read_text().splitlines()


def get_bit_occurences(in_data):
    bit_occurences = [0] * 12
    for line in in_data:
        for idx, val in enumerate(line.strip()):
            bit_occurences[idx] += 1 if int(val) == 1 else -1
    return bit_occurences


def filter_bit(bit_idx, in_data, op):
    most_common_val = 1 if op(get_bit_occurences(in_data)[bit_idx], 0) else 0

    new_data = [entry.strip() for entry in in_data if int(entry[bit_idx]) != most_common_val]
    if not new_data:
        return [in_data[-1]]
    return new_data if new_data else [in_data[-1]]


def get_filtered_out(op):
    filtered = data
    idx = 0
    while len(filtered) > 1:
        print(idx)
        filtered = filter_bit(idx, filtered, op)
        idx += 1
    return int(filtered[0], 2)


oxygen_generator_rating = get_filtered_out(operator.ge)
co2_scrubber_rating = get_filtered_out(operator.lt)
print(oxygen_generator_rating, co2_scrubber_rating)
print(oxygen_generator_rating * co2_scrubber_rating)

