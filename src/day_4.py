from typing import Dict
from utils import read_input, create_grid, Coordinate

PAPER_ROLL = '@'

def is_paper_roll(cell: str) -> bool:
    """Checks whether a string is a @"""
    return cell == PAPER_ROLL

def can_access(position: Coordinate, grid: Dict[Coordinate, str]) -> bool:
    """Given a position and sparse grid,
    checks whether the position has less than 4
    paper rolls in its 8 neighbouring cells"""
    MAX_ALLOWED_NEIGHBOURS = 4
    if position not in grid:
        return False

    # Deltas for each neighbour, going clock-wise
    # from top-left
    neighbours = [
        (-1, -1), (0, -1), (1, -1), (1, 0),
        (1, 1), (0, 1), (-1, 1), (-1, 0)
    ]

    neighbouring_rolls = 0
    for dx, dy in neighbours:
        neighbour = Coordinate(x=position.x+dx, y=position.y+dy)
        if neighbour in grid:
            neighbouring_rolls += 1

    return neighbouring_rolls < MAX_ALLOWED_NEIGHBOURS

def part_1() -> int:
    """How many rolls of paper can be accessed by a forklift?"""
    inputs = read_input(4, list)
    grid = create_grid(inputs, predicate=is_paper_roll)

    accessible_rolls = 0
    for pos in grid:
        if can_access(pos, grid):
            accessible_rolls += 1
    return accessible_rolls

def part_2() -> int:
    """How many rolls of paper in total can be removed by the Elves and their forklifts?
    
    This time, once a batch of rolls has been removed, another batch will be removed as
    long as there are accessible rolls."""
    inputs = read_input(4, list)
    grid = create_grid(inputs, predicate=is_paper_roll)

    was_removed = 0
    while True:
        to_remove = {}
        for pos in grid:
            if can_access(pos, grid):
                was_removed += 1
                to_remove[pos] = PAPER_ROLL
        if to_remove:
            grid = dict(grid.items() - to_remove.items())
        else:
            break
    return was_removed

if __name__ == '__main__':
    part_1_result = part_1()
    print(f'Part 1: {part_1_result}')
    assert part_1_result == 1547

    part_2_result = part_2()
    print(f'Part 2: {part_2_result}')
    assert part_2_result == 8948