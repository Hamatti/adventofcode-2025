from utils import read_input
from typing import Tuple

def mapper(line: str) -> Tuple[str, int]:
    """Input lines are in format of
    XY where 
    - X is direction of either 'R' or 'L' and
    - Y is a positive integer

    Returns a tuple of (direction, amount)
    """
    direction = line[0]
    amount = int(line[1:])

    return direction, amount

def part_1() -> int:
    """
    Calculate how many times the dial stops at 0
    at the end of an instruction.
    """
    rotations = read_input(1, mapper)
    current = 50
    hits_at_zero = 0

    for direction, amount in rotations:
        if direction == 'L':
            current -= amount
        elif direction == 'R':
            current += amount

        # Keep values within bounds of 0—99
        current %= 100
        
        if current == 0:
            hits_at_zero += 1

    return hits_at_zero

def part_2_simple() -> int:
    """
    Calculate how many times the dial hits 0
    during an instruction.
    """
    rotations = read_input(1, mapper)
    current = 50

    hits_at_zero = 0
    for direction, amount in rotations:
        if direction == 'L':
            multiplier = -1
        elif direction == 'R':
            multiplier = 1

        for i in range(amount):
            current += multiplier
            current %= 100
            
            if current == 0:
                hits_at_zero += 1

    return hits_at_zero

def part_2() -> int:
    """
    Calculate how many times the dial hits 0
    during an instruction.
    """
    rotations = read_input(1, mapper, example=False)
    current = 50

    hits_at_zero = 0
    for direction, amount in rotations:
        prev = current

        full_rotations, leftover = divmod(amount, 100)
        hits_at_zero += full_rotations

        if direction == 'L':
            current -= leftover
        elif direction == 'R':
            current += leftover

        # We've hit 0:
        #  If we go over 100
        if current > 100:
            hits_at_zero += 1
        #  If we go below 0 (and didn't start at 0)
        elif current < 0 and prev != 0:
            hits_at_zero += 1
        #  If we land on exactly zero
        elif current % 100 == 0:
            hits_at_zero += 1
        
        current %= 100

    return hits_at_zero

if __name__ == '__main__':
    part_1_result = part_1()
    print(f'Part 1: {part_1_result}')
    assert part_1_result == 1043, 'Incorrect answer for part 1'

    part_2_result = part_2()
    print(f'Part 2: {part_2_result}')
    assert part_2_result == 5963, 'Incorrect answer for part 2'
