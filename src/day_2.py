import re
from typing import List, Tuple

from utils import read_input

INVALID_ID_PATTERN = r'^(\d+)\1$'
INVALID_ID_PATTERN_2 = r'^(\d+)(\1)+$'

def mapper(line: str) -> List[Tuple[int, int]]:
    """Reads a line of integer rangers, divided by commas"""
    ranges = []
    for r in line.split(','):
        start, end = [int(p) for p in r.split('-')]
        ranges.append((start, end))
    return ranges

def is_invalid(product_id: int) -> re.Match[str] | None:
    """Checks if product_id is made of two repeated strings"""
    return re.search(INVALID_ID_PATTERN, str(product_id))

def is_invalid_p2(product_id: int) -> bool:
    """Checks if product_id is made of a string, repeated at least twice"""
    return re.search(INVALID_ID_PATTERN_2, str(product_id))


def part_1() -> int:
    """Calculate the sum of all invalid product ids.
    
    A product id is invalid if it's made of two repeating numbers."""
    data = read_input(2, mapper)[0]
    invalid_id_sum = 0
    for start, end in data:
        for product_id in range(start, end+1):
            if is_invalid(product_id):
                invalid_id_sum += product_id

    return invalid_id_sum

def part_2() -> int:
    """Calculate the sum of all invalid product ids.
    
    A product id is invalid if it's made of 
    at least two repeating numbers."""
    data = read_input(2, mapper)[0]
    invalid_id_sum = 0
    for start, end in data:
        for product_id in range(start, end+1):
            if is_invalid_p2(product_id):
                invalid_id_sum += product_id

    return invalid_id_sum


if __name__ == '__main__':
    part_1 = part_1()
    print(f'Part 1: {part_1}')
    assert part_1 == 38158151648
    
    part_2 = part_2()
    print(f'Part 2: {part_2}')
    assert part_2 == 45283684555
