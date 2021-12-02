import operator

class Position:
    horizontal: int = 0
    depth: int = 0
    aim: int = 0

    def process_command(self, command: str, val: int):
        if command == "forward":
            self.horizontal += val
            self.depth += self.aim * val 
        else:
            self.aim += (val if command == "down" else -val)
    
position = Position()
with open("test-data.txt") as f:
    while line := f.readline():
        command, num = line.strip().split()
        position.process_command(command, int(num))

print(position.horizontal * position.depth)


