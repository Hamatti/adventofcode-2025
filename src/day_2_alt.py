from typing import List, Tuple

from utils import read_input


def mapper(line: str) -> List[Tuple[int, int]]:
    """Reads a line of integer rangers, divided by commas"""
    ranges = []
    for r in line.split(','):
        start, end = [int(p) for p in r.split('-')]
        ranges.append((start, end))
    return ranges

def part_2() -> int:
    ranges = read_input(2, mapper)[0]
    
    invalid_ids = 0

    for start, end in ranges:
        for num in range(int(start), int(end)+1):
            original = str(num)

            for i in range(len(original)//2, 0, -1):
                substring = original[:i]
                multiplier = len(original) // len(substring)
                if substring * multiplier == original:
                    invalid_ids += num
                    break

    return invalid_ids

if __name__ == '__main__':    
    part_2_result = part_2()
    print(f'Part 2: {part_2_result}')
    assert part_2_result == 45283684555
    
