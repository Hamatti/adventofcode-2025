from collections import defaultdict
from copy import copy

from utils import read_input, create_grid, Coordinate


START = 'S'
SPLITTER = '^'
EMPTY = '.'

def is_not_empty(cell: str) -> bool:
    return cell != EMPTY

def find_start_position(grid: dict[Coordinate, str]) -> Coordinate:
    """Find a coordinate in the grid for starting positions"""
    for position, value in grid.items():
        if value == START:
            return position
    
    raise ValueError('No start position found')

def part_1() -> int:
    """Calculate how many times beams get split
    when they start from a START position and move downwards."""
    inputs = read_input(7, str)
    grid = create_grid(inputs, predicate=is_not_empty)
    
    start = find_start_position(grid)
    bottom = len(inputs)
    beams = set([start.x])
    split_count = 0

    for row in range(1, bottom+1):
        new_beams = set()
        for col in beams:
            hits_splitter = Coordinate(x=col, y=row) in grid
            if hits_splitter:
                new_beams.add(col-1)
                new_beams.add(col+1)
                split_count += 1
            else:
                new_beams.add(col)
        beams = new_beams

    return split_count

def part_2() -> int:
    inputs = read_input(7, str)
    grid = create_grid(inputs, predicate=is_not_empty)
    start = find_start_position(grid)
    beam_columns = defaultdict(int)
    beam_columns[start.x] = 1
    bottom = len(inputs)
    
    for row in range(1, bottom+1):
        new_beam_columns = copy(beam_columns)
        for col in beam_columns:
            hits_splitter = Coordinate(x=col, y=row) in grid
            if hits_splitter:
                new_beam_columns[col-1] += new_beam_columns[col]
                new_beam_columns[col+1] += new_beam_columns[col]
                del new_beam_columns[col]
        beam_columns = new_beam_columns
    
    return sum(value for value in beam_columns.values()) 


if __name__ == '__main__':
    part_1_result = part_1()
    print(f'Part 1: {part_1_result}')
    assert part_1_result == 1690
    
    part_2_result = part_2()
    print(f'Part 2: {part_2_result}')
    assert part_2_result == 221371496188107
    
