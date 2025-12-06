from dataclasses import dataclass
from math import prod
from typing import List, Literal, Tuple

INPUT_FILE = '../inputs/day_6.txt'

@dataclass
class Equation:
    operation: Literal['*', '+']
    numbers: List[int]

    def calculate(self) -> int:
        match self.operation:
            case '*':
                return prod(self.numbers)
            case '+':
                return sum(self.numbers)
            case _:
                raise NotImplementedError(f'Unknown opeator {self.operation}')


def convert_column(cursor: int, data) -> Tuple[str|None, int]:
    number = ''
    op = None

    for line in data:
        char = line[cursor]
        if char == ' ': continue
        if char in ('*', '+'):
            op = char
            break
        number += char

    return op, int(number)

def read_equations() -> List[Equation]:
    equations = []

    with open(INPUT_FILE, 'r') as inputfile:
        data = inputfile.read().split('\n')
    
    cursor = len(data[0]) - 1
    numbers = []

    while cursor >= 0:
        op, number = convert_column(cursor, data)
        numbers.append(number)
        cursor -= 1
        if op:
            equations.append(Equation(op, numbers))
            numbers = []
            cursor -= 1
            continue
    
    return equations

def part_2() -> int:
    equations = read_equations()
    return sum(eq.calculate() for eq in equations)


part_2_result = part_2()
print(f'Part 2: {part_2_result}')
assert part_2_result == 9627174150897