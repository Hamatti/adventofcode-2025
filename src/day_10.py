import re
from collections import namedtuple
from dataclasses import dataclass
from itertools import combinations_with_replacement
from typing import List

from utils import read_input

LIGHTS_PATTERN = r"\[(.*)\]"
BUTTON_PATTERN = r"\(.*\)"
JOLTAGE_PATTERN = r"\{.*\}"

Machine = namedtuple("Machine", ["lights", "lights_length", "buttons", "joltage"])


def mapper(line: str) -> Machine:
    lights_binary: str = (
        re.match(LIGHTS_PATTERN, line).groups()[0].replace("#", "1").replace(".", "0")
    )
    buttons: List[str] = re.findall(BUTTON_PATTERN, line)[0].split(" ")
    buttons: List[str] = [
        btn.replace("(", "").replace(")", "").split(",") for btn in buttons
    ]
    joltage: List[int] = [
        int(num)
        for num in re.findall(JOLTAGE_PATTERN, line)[0]
        .replace("{", "")
        .replace("}", "")
        .split(",")
    ]

    buttons_binaries = []
    for button in buttons:
        button_binary = ""
        for i in range(len(lights_binary)):
            button_binary += "1" if str(i) in button else "0"
        buttons_binaries.append(button_binary)

    return Machine(int(lights_binary, 2), len(lights_binary), buttons_binaries, joltage)


def part_1() -> int:
    instructions = read_input(10, mapper)
    all_presses = 0

    for instruction in instructions:
        target = instruction.lights
        presses = 1
        stop = False
        while not stop:
            possible_presses = combinations_with_replacement(
                instruction.buttons, presses
            )

            for button_presses in possible_presses:
                machine = int("0" * instruction.lights_length, 2)
                for _press in button_presses:
                    machine ^= int(_press, 2)
                if machine == target:
                    all_presses += presses
                    stop = True
                    break
            presses += 1

    return all_presses


if __name__ == "__main__":
    part_1_result = part_1()
    print(f"Part 1: {part_1_result}")
    assert part_1_result == 469
