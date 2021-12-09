from pathlib import Path
from dataclasses import dataclass
from itertools import chain
from pprint import pprint

test_data = Path("test-data.txt").read_text()
test_data = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

test_data = test_data.splitlines()


@dataclass
class DigitMatches:
    first_digit: int
    second_digit: int
    unique_characters: set


digits = [
    ["a", "b", "c", "e", "f", "g"],
    ["c", "f"],
    ["a", "c", "d", "e", "g"],
    ["a", "c", "d", "f", "g"],
    ["b", "c", "d", "f"],
    ["a", "b", "d", "f", "g"],
    ["a", "b", "d", "e", "f", "g"],
    ["a", "c", "f"],
    ["a", "b", "c", "d", "e", "f", "g"],
    ["a", "b", "c", "d", "f", "g"],
]

matches = {}


def get_unique_length_digits(curr_digits):
    lengths = [len(digit) for digit in curr_digits]
    return {idx for idx, length in enumerate(lengths) if lengths.count(length) == 1}


def get_unique_lengths(curr_digits):
    lengths = [len(digit) for digit in curr_digits]
    return {length for length in lengths if lengths.count(length) == 1}


def create_updated_digits(curr_digits, matches):
    return [
        [sign for sign in digit if sign not in set(matches.values())]
        for digit in curr_digits
    ]


signal_lines = [val.split(" | ")[0] for val in test_data]


def get_unique_val(signals, relevant_lengths):
    for signal in filter(lambda x: len(x) in relevant_lengths, signals):
        for other_signal in signals:
            diff = set(signal).symmetric_difference(set(other_signal))
            if len(diff) == 1:
                return signal, other_signal, diff


def get_digit_at_len(curr_digits, length):
    for digit in curr_digits:
        if len(digit) == length:
            return digit


curr_signal_line = signal_lines[0]
updated_digits = create_updated_digits(digits, matches)
pprint(updated_digits)
print(curr_signal_line)
while curr_signal_line:
    unique_lengths = get_unique_lengths(updated_digits)
    pprint(unique_lengths)
    signal, other_signal, diff = get_unique_val(
        curr_signal_line.split(), unique_lengths
    )
    unique_lengths_digits = get_unique_length_digits(updated_digits)
    first_digit = get_digit_at_len(updated_digits, len(signal))
    second_digit = get_digit_at_len(updated_digits, len(other_signal))

    print("SIGNALS")
    print(signal, other_signal, diff)
    pprint(updated_digits)
    unique_val_between_digits = set(first_digit).symmetric_difference(set(second_digit))
    matched = diff.pop()
    print(matched)
    matched_digit = unique_val_between_digits.pop()
    print(matched_digit)
    matches[matched] = matched_digit
    print("MATCHES")
    pprint(matches)
    updated_digits = create_updated_digits(updated_digits, matches)
    pprint(updated_digits)
    curr_signal_line = curr_signal_line.replace(matched, "")
    print(curr_signal_line)


# def find_len(len_to_find, signals):
#
#
# signal_lines = signals
#
# signals = signal_lines[0].split()
# first_digit =
# relevant_signals = [signal for signal in signal_lines[0].split() if len(signal) in lengths_to_search]
#
# print(f"{relevant_signals=}")
