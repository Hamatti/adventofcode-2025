# /// script
# requires-python = ">=3.10"
# dependencies = [
#    "z3-solver",
# ]
# ///


import re
from collections import namedtuple
from itertools import combinations
from typing import List

import z3

from utils import read_input

LIGHTS_PATTERN = r"\[(.*)\]"
BUTTON_PATTERN = r"\(.*\)"
JOLTAGE_PATTERN = r"\{.*\}"

Machine = namedtuple("Machine", ["lights", "buttons", "button_raw", "joltage"])


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

    return Machine(int(lights_binary, 2), buttons_binaries, buttons, joltage)


def part_1() -> int:
    machines = read_input(10, mapper)
    all_presses = 0

    for machine in machines:
        target = machine.lights
        presses = 1
        stop = False
        while not stop:
            possible_presses = combinations(
                machine.buttons, presses
            )

            for button_presses in possible_presses:
                current_lights = 0
                for _press in button_presses:
                    current_lights ^= int(_press, 2)
                if current_lights == target:
                    all_presses += presses
                    stop = True
                    break
            presses += 1

    return all_presses

def part_2() -> int:
    machines = read_input(10, mapper)
    min_number_of_presses = 0
    for machine in machines:
        optimizer = z3.Optimize()
        presses = [z3.Int(f"push-button-{idx}") for idx in range(len(machine.button_raw))]

        for idx, _ in enumerate(machine.button_raw):
            optimizer.add(presses[idx] >= 0)
        for idx, _ in enumerate(machine.joltage):
            optimizer.add(
                sum(presses[j] for j, btn in enumerate(machine.button_raw) if str(idx) in btn)
                == machine.joltage[idx]
            )

        optimizer.minimize(sum(presses))
        assert optimizer.check() == z3.sat

        model = optimizer.model()
        for press in presses:
            min_number_of_presses += model[press].as_long()

    return min_number_of_presses

if __name__ == "__main__":
    part_1_result = part_1()
    print(f"Part 1: {part_1_result}")
    assert part_1_result == 469
    
    part_2_result = part_2()
    print(f"Part 1: {part_2_result}")
    assert part_2_result == 19293
