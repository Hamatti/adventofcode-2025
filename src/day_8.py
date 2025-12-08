from utils import read_input
from dataclasses import dataclass
from math import sqrt
from itertools import combinations

@dataclass
class JunctionBox:
    x: int
    y: int
    z: int
    circuit: set[JunctionBox]

    def distance(self, other: JunctionBox) -> JunctionBox:
        """Calculate Euclidian distance between two boxes"""
        return sqrt((self.x - other.x)**2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)
    
    def connect(self, other: JunctionBox):
        """Connect two JunctionBoxes in a way where 
        every connection between nodes is shared."""
        # Create a new circuit of self, other and all boxes connected to either
        circuit = self.circuit | {other} | other.circuit | {self}

        # Update circuit information to all 
        for box in circuit:
            box.circuit = circuit

    def __gt__(self, other: JunctionBox) -> bool:
        return len(self) > len(other)
    
    def __lt__(self, other: JunctionBox) -> bool:
        return len(self) < len(other)
    
    def __hash__(self):
        return self.x * 1001 + self.y * 2002 + self.z * 3003
    
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z}): {len(self.circuit)}'
    
    def __len__(self):
        return len(self.circuit)
    
@dataclass
class JunctionBoxPair:
    one: JunctionBox
    other: JunctionBox

    def connect(self):
        self.one.connect(self.other)

    def __gt__(self, other: JunctionBoxPair) -> bool:
        return self.one.distance(self.other) > other.one.distance(other.other)
    
    def __lt__(self, other:  JunctionBoxPair) -> bool:
        return self.one.distance(self.other) < other.one.distance(other.other)

def mapper(line: str) -> JunctionBox:
    x, y, z = [int(coord) for coord in line.split(',')]
    return JunctionBox(x=x, y=y, z=z, circuit=set())
    
def part_1() -> int:
    boxes = read_input(8, mapper)
    MAX_CONNECTIONS = 1000

    all_pairs = sorted([JunctionBoxPair(a, b) for a, b in combinations(boxes, 2)])
    for pair in all_pairs[:MAX_CONNECTIONS]:
        pair.connect()

    biggest_circuits = sorted(boxes, reverse=True)
    prod = 1
    circuits_seen = []
    unique_circuits_counted = 0
    for box in biggest_circuits:
        if box.circuit in circuits_seen:
            continue
        circuits_seen.append(box.circuit)
        prod *= len(box)
        unique_circuits_counted += 1

        if unique_circuits_counted == 3:
            break
    return prod

def part_2() -> int:
    boxes = read_input(8, mapper)
    all_pairs = sorted([JunctionBoxPair(a, b) for a, b in combinations(boxes, 2)])

    for pair in all_pairs:
        pair.connect()
        if len(pair.one) == len(boxes):
            break

    return pair.one.x * pair.other.x


if __name__ == '__main__':
    part_1_result = part_1()
    print(f'Part 1: {part_1_result}')
    assert part_1_result == 83520

    part_2_result = part_2()
    print(f'Part 2: {part_2_result}')
    assert part_2_result == 1131823407