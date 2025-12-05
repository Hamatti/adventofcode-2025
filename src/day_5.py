from typing import List, Tuple

from utils import read_multisection_input
from collections import namedtuple

Range = namedtuple('Range', ['start', 'end'])

def map_upper_section(section: str) -> List[Range]:
    """Takes a section of ranges and turns them into
    Range tuples"""
    lines = section.split('\n')
    ranges = []
    for line in lines:
        start, end = [int(num) for num in line.split('-')]
        ranges.append(Range(start, end))
    return ranges

def map_lower_section(section: str) -> List[int]:
    """Splits input with new lines and turns every
    line into an integer"""
    return [int(num) for num in section.split('\n')]

def is_fresh(ingredient: int, ranges: List[Range]) -> bool:
    """Checks if ingredient is in any of the provided ranges"""
    for range in ranges:
        if range.start <= ingredient <= range.end:
            return True
    return False

def part_1() -> int:
    """Calculate how many ingredients in the second half are 
    included in any of the ranges from the first half"""
    ranges, ingredients = read_multisection_input(5, [map_upper_section, map_lower_section])
    fresh_count = 0
    for ingredient in ingredients:
        if is_fresh(ingredient, ranges):
            fresh_count += 1
    return fresh_count

def try_to_combine(first: Range, second: Range) -> Range|Tuple[Range, Range]:
    """Tries to combine two ranges. If ranges overlap, returns a single Range.
    
    If they don't overlap, return both Ranges."""
    if first.end >= second.start:
        end = first.end if first.end > second.end else second.end
        return Range(start=first.start, end=end)
    else:
        return (first, second)

def part_2() -> int:
    """Calculate how many ids are included in all the ranges"""
    ranges, _ = read_multisection_input(5, [map_upper_section, lambda x: x])
    
    # Sort ranges by start value so they can be combined
    ranges = sorted(ranges, key=lambda x: x.start)
    
    index = 0
    while True:
        try:
            combo = try_to_combine(ranges[index], ranges[index+1])
            if isinstance(combo, Range):
                ranges[index] = combo
                ranges.remove(ranges[index+1])
            else:
                index += 1

        except IndexError:
            break

    return sum(end - start + 1 for start, end in ranges)
    
if __name__ == '__main__':
    part_1_result = part_1()
    print(f'Part 1: {part_1_result}')
    assert part_1_result == 698

    part_2_result = part_2()
    print(f'Part 2: {part_2_result}')
    assert part_2_result == 352807801032167
