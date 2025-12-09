from utils import read_input, Coordinate
from itertools import combinations, pairwise
from typing import Tuple


def mapper(line: str) -> Coordinate:
    x, y = [int(num) for num in line.split(',')]
    return Coordinate(x, y)

def calculate_area(c1: Coordinate, c2: Coordinate) -> int:
    return (abs(c1.x - c2.x) + 1) * (abs(c1.y - c2.y) + 1)

def part_1() -> int:
    coordinates = read_input(9, mapper)
    largest = 0

    for c1, c2 in combinations(coordinates, 2):
        area = (abs(c1.x - c2.x) + 1) * (abs(c1.y - c2.y) + 1)
        if area > largest:
            largest = area
    return largest

def intersects(c1: Coordinate, c2: Coordinate, line: Tuple[Coordinate, Coordinate]) -> bool:
    """Checks if a line between two coordinates intersects with a rectangle drawn between
    opposite corners c1 and c2"""
    # Boundaries of the rectangle
    rect_left = min(c1.x, c2.x)
    rect_right = max(c1.x, c2.x)
    rect_top = min(c1.y, c2.y)
    rect_bottom = max(c1.y, c2.y)
    
    l1, l2 = line

    # Positions of the line
    # If line is vertical, line_right == line_left
    # If line is horizontal, line_top == line_bottom
    line_right = max(l1.x, l2.x)
    line_left = min(l1.x, l2.x)
    line_bottom = max(l1.y, l2.y)
    line_top = min(l1.y, l2.y)

    if line_right == line_left:
        vertical_line_is_inside = rect_right > line_right > rect_left
        is_within_box_horizontally = line_bottom > rect_top and rect_bottom > line_top
        return vertical_line_is_inside and is_within_box_horizontally

    else:
        horizontal_line_is_inside = rect_bottom > line_top > rect_top
        is_within_box_vertically = rect_right > line_left and line_right > rect_left
        return horizontal_line_is_inside and is_within_box_vertically
        

def part_2() -> int:
    coordinates = read_input(9, mapper)
    
    areas = [(c1, c2, calculate_area(c1, c2)) for c1, c2 in combinations(coordinates, 2)]
    areas_by_size = sorted(areas, key=lambda x: x[2], reverse=True)
    lines = list(pairwise(coordinates + [coordinates[0]]))

    for c1, c2, area in areas_by_size:
        # Does any of the lines in input cross through our rectangle?
        # If it does, part of the area is outside and we go to the next area
        if any(intersects(c1, c2, line) for line in lines):
            continue

        # If none intersect, we found a winner
        return area

if __name__ == '__main__':
    part_1_result = part_1()
    print(f'Part 1: {part_1_result}')
    assert part_1_result == 4776100539
    
    part_2_result = part_2()
    print(f'Part 2: {part_2_result}')
    assert part_2_result == 1476550548
    
