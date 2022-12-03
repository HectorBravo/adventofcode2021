# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 2 excercise 2 https://adventofcode.com/2021/day/2#part2

import adv2021_common as common

def process_contents(contents):
    # print(contents)
    result = 0
    horizontal_position = 0
    depth = 0
    aim = 0
    for pair in contents:
        direction, value = pair.split()
        value = int(value)
        if direction == 'forward':
            horizontal_position += value
            depth += (aim * value)
        elif direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value
    result = horizontal_position * depth
    return result

if __name__ == "__main__":
    contents = common.read_input()
    result = process_contents(contents)
    common.print_result(result, 2015547716)