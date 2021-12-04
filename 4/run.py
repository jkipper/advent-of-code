import pathlib
import itertools


class Board:
    line_length = 5
    board = []
    won = False

    def __init__(self, board):
        self.board = board

    def iter_rows_and_colums(self):
        for idx in range(self.line_length):
            row_start = idx * self.line_length
            yield self.board[row_start : row_start + self.line_length]
            yield self.board[idx :: self.line_length]

    def has_bingo(self, called_numbers):
        self.won = any(set(values).issubset(called_numbers) for values in self.iter_rows_and_colums())
        return self.won

    def calculate_score(self, last_number, called_numbers):
        return sum(filter(lambda number: number not in called_numbers, self.board)) * last_number


def get_next_board_data(i):
    return list(
        itertools.chain.from_iterable([[int(num) for num in line.split()] for line in itertools.takewhile(bool, i)])
    )


test_data = pathlib.Path("test-data.txt").read_text().splitlines()

iterator = iter(test_data)
generated_numbers = [int(val) for val in next(iterator).split(",")]
next(iterator)


boards = []
while board := get_next_board_data(iterator):
    boards.append(Board(board))

called_numbers = set()
for number in generated_numbers:
    called_numbers.add(number)

    for board in filter(lambda x: not x.won, boards):
        if board.has_bingo(called_numbers) and all(b.won for b in boards):
            print(board.calculate_score(number, called_numbers))
            exit()
