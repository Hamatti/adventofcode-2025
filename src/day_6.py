from collections import defaultdict
from dataclasses import dataclass
from math import prod
from typing import List, Literal

from utils import read_input


INPUT_FILE = '../inputs/day_6.txt'

@dataclass
class CephalopodCalculation:
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

def mapper(line: str) -> List[int]|List[str]:
    """Reads either a line of numbers or a line of +/* characters"""
    parts = line.split()
    try:
        return [int(elem) for elem in parts]
    except ValueError:
        return parts

    
def part_1() -> int:
    """Calculate sums and products of column based equations"""
    data = read_input(6, mapper)
    calculations = zip(*data)

    total = 0
    for calc in calculations:
        total += CephalopodCalculation(calc[-1], calc[:-1]).calculate()
    return total

def reparse(data: List) -> List[List[str]]:
    # Read input file into list of lines
    with open(INPUT_FILE, 'r') as inputfile:
        raw_data = inputfile.readlines()
    
    correct_calculations = []

    # Current block's start offset
    cursor = 0

    for block in data:
        # Calculate how wide a block is by finding the longest 
        # string representation of numbers in block
        block_length = max(len(str(num)) for num in block[:-1])

        # Read block_length characters with spaces preserved
        calculation = []
        for line in raw_data:
            item = line[cursor:cursor+block_length]
            calculation.append(item)
        correct_calculations.append(calculation)

        # Move cursor to the start of next block
        # +1 is required to take into account
        # the space between blocks
        cursor = cursor + block_length + 1
    
    return correct_calculations

def convert_to_cephalopod_math(blocks: List[List[str]]) -> List[CephalopodCalculation]:
    """Convert column-based data blocks into CephalopodCalculations"""
    calculations = []
    for block in blocks:
        operation = block[-1].strip()
        numbers = defaultdict(str)
        for entry in block[:-1]:
            for col, value in enumerate(entry):
                if value == ' ':
                    continue
                numbers[col] += value
                
        calculations.append(CephalopodCalculation(operation, [int(num) for num in numbers.values()]))
    
    return calculations

def part_2() -> int:
    raw_input = read_input(6, mapper)
    data = zip(*raw_input)

    blocks = reparse(data)
    calculations = convert_to_cephalopod_math(blocks)
    total = 0
    for calc in calculations:
        total += calc.calculate()
    return total


if __name__ == '__main__':
    part_1_result = part_1()
    print(f'Part 1: {part_1_result}')
    assert part_1_result == 5381996914800
    
    part_2_result = part_2()
    print(f'Part 2: {part_2_result}')
    assert part_2_result == 9627174150897