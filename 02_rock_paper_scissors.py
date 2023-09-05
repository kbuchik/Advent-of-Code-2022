#!/usr/bin/python3

## Advent of Code 2022 - Calorie Counting
## https://adventofcode.com/2022/day/1

import os
import sys

shapeScore = {'X': 1, 'Y': 2, 'Z': 3}
roundScore = {
    'A X': 3, 'A Y': 6, 'A Z': 0,
    'B X': 0, 'B Y': 3, 'B Z': 6,
    'C X': 6, 'C Y': 0, 'C Z': 3,
}
strategyMap = {
    'A X': 'Z', 'A Y': 'X', 'A Z': 'Y',
    'B X': 'X', 'B Y': 'Y', 'B Z': 'Z',
    'C X': 'Y', 'C Y': 'Z', 'C Z': 'X',
}

p1Score = 0
p2Score = 0

with open("input02.txt") as f:
    for line in f:
        points = 0
        line = line.rstrip()
        if line:
            p1Score += shapeScore[line[2]]
            p1Score += roundScore[line]
            shape = strategyMap[line]
            p2Score += shapeScore[shape]
            p2Score += roundScore[line[0:2] + shape]

print("Part One:")
print(str(p1Score) + "\n")
print("Part Two:")
print(str(p2Score) + "\n")

exit(0)
