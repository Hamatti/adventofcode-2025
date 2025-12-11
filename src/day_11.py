from typing import List, Tuple
from functools import cache

from utils import read_input

EXIT_NODE = 'out'
P1_START_NODE = 'you'
P2_START_NODE = 'svr'

def mapper(line: str) -> Tuple[str, List[str]]:
    root, nodes = line.split(': ')
    nodes = nodes.split(' ')

    return root, nodes

def find_path(root: str, nodes: dict[str, List[str]]) -> int:
    if EXIT_NODE in nodes[root]:
        return 1

    ways = 0
    for node in nodes[root]:
        ways += find_path(node, nodes)
    return ways

def part_1() -> int:
    """Calculate in how many ways you can reach node EXIT_NODE
    when starting from node P1_START_NODE."""
    data = read_input(11, mapper)
    tree = {}
    for root, nodes in data:
        tree[root] = nodes

    return find_path(P1_START_NODE, tree)


@cache
def fft_dac_path(root: str, nodes: Tuple[str, Tuple[str, ...]], seen_fft: bool=False, seen_dac:bool=False) -> int:
    """Follow the path from root node until EXIT_NODE node.
    
    If a path contains both 'dac' and 'fft' nodes, count it,
    otherwise ignore it."""
    seen_dac = seen_dac or root == 'dac'
    seen_fft = seen_fft or root == 'fft'
 
    next_nodes = [n for r, n in nodes if r == root][0]
    
    if EXIT_NODE in next_nodes:
        if seen_fft and seen_dac:
            return 1
        else:
            return 0
    
    valid_paths = 0
    for node in next_nodes:
        valid_paths += fft_dac_path(node, nodes, seen_fft, seen_dac)
    
    return valid_paths

def part_2() -> int:
    """Starting from P2_START_NODE, calculate how many
    ways there are to reach EXIT_NODE while visiting both
    'fft' and 'dac'"""
    data = read_input(11, mapper)
    tree = []
    for root, nodes in data:
        tree.append((root, tuple(nodes)))
    tree = tuple(tree)
    
    valid_paths = fft_dac_path(P2_START_NODE, tree)
    return valid_paths
    

if __name__ == '__main__':
    part_1_result = part_1()
    print(f'Part 1: {part_1_result}')
    assert part_1_result == 428
    
    part_2_result = part_2()
    print(f'Part 2: {part_2_result}')
    assert part_2_result == 331468292364745
    
