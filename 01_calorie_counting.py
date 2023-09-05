#!/usr/bin/python3

## Advent of Code 2022
## Day 1 - Calorie Counting
## https://adventofcode.com/2022/day/1

import os
import sys

elves = list()

with open("input01.txt") as f:
    cals = 0
    for line in f:
        line = line.rstrip()
        if line:
            cals += int(line)
        else:
            elves.append(cals)
            cals = 0
elves.sort(reverse=True)

print("Part One:")
print(str(elves[0]) + "\n")

print("Part Two:")
print(str(sum(elves[0:3])) + "\n")

exit(0)
