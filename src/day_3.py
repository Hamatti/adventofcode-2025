from typing import List
from utils import read_input

type BatteryBank = List[int]

def mapper(line: str) -> BatteryBank:
    """Turn string of digits into a list of integers"""
    return [int(num) for num in line]

def calculate_max_joltage(bank: BatteryBank) -> int:
    """Calculates the highest possible joltage
    of a battery bank when exactly 2 batteries
    are turned on.

    A joltage is the combined value of the joltages
    of those batteries.

    For example, turning on batteries with joltages
    of 9 and 4 gives total joltage of 94.
    """
    first = max(bank[:-1])
    second = max(bank[bank.index(first)+1:])
    return int(f'{first}{second}')

def calculate_12_joltage(bank: BatteryBank) -> int:
    """Calculates the highest possible joltage
    of a battery bank when exactly 12 batteries
    are turned on.

    A joltage is the combined value of the joltages
    of those batteries.

    For example, turning on batteries with joltages
    of 9 and 4 gives total joltage of 94.
    """
    joltage = ''
    for i in range(11, 0, -1):
        next_largest_battery = max(bank[:-i])
        bank = bank[bank.index(next_largest_battery)+1:]
        joltage += str(next_largest_battery)

    # And one more for good measure
    joltage += str(max(bank))

    return int(joltage)

def part_1() -> int:
    """Calculate the combined joltage of
    all battery banks when 2 batteries are turned on
    for each one."""
    battery_banks = read_input(3, mapper)
    total_joltage = 0
    for bank in battery_banks:
        total_joltage += calculate_max_joltage(bank)
    return total_joltage

def part_2() -> int:
    """Calculate the combined joltage of
    all battery banks when 12 batteries are turned on
    for each one."""
    battery_banks = read_input(3, mapper)
    total_joltage = 0
    for bank in battery_banks:
        total_joltage += calculate_12_joltage(bank)
    return total_joltage
        

if __name__ == '__main__':
    part_1_result = part_1()
    print(f'Part 1: {part_1_result}')
    assert part_1_result == 17443

    part_2_result = part_2()
    print(f'Part 2: {part_2_result}')
    assert part_2_result == 172167155440541