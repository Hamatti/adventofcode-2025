from dataclasses import dataclass
from collections import namedtuple
from typing import List

from utils import read_multisection_input, Coordinate

Present = namedtuple('Present', ['area', 'coordinates'])
Tree = namedtuple('Tree', ['width', 'height', 'presents', 'area'])

def present_mapper(section: str) -> Present:
    lines = section.split('\n')[1:]
    coordinates: set[Coordinate] = set()
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            if lines[y][x] == '#':
                coordinates.add(Coordinate(x=x, y=y))
    return Present(len(coordinates), coordinates)


def trees_mapper(section: str) -> List[Tree]:
    trees = []
    for line in section.split('\n'):
        size, presents = line.split(': ')
        size = size.split('x')
        width, height = int(size[0]), int(size[1])
        presents = [int(p) for p in presents.split(' ')]
        trees.append(Tree(width, height, presents, width * height))
    return trees

def part_1() -> int:
    data = read_multisection_input(12, [present_mapper] * 6 + [trees_mapper])
    presents = data[:-1]
    trees = data[-1]
    
    valid_trees = 0

    for tree in trees:
        area_needed = 0
        for index, count in enumerate(tree.presents):
            area_needed += count * presents[index].area
        if tree.area >= area_needed:
            valid_trees += 1
    
    return valid_trees

def part_2() -> int:
    """There is no ~~spoon~~ part 2. Merry Christmas!"""
    ...

if __name__ == '__main__':
    part_1_result = part_1()
    print(f'Part 1: {part_1_result}')
    assert part_1_result == 440