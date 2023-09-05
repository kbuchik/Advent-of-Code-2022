#!/usr/bin/python3

## Advent of Code 2022
## Day 4 - Camp Cleanup
## https://adventofcode.com/2022/day/4

import os
import sys

count1 = 0
count2 = 0

with open("input04.txt") as f:
    for line in f:
        line = line.rstrip()
        pairs = line.split(',')
        a = int(pairs[0].split('-')[0])
        b = int(pairs[0].split('-')[1])
        c = int(pairs[1].split('-')[0])
        d = int(pairs[1].split('-')[1])
        if ((a <= c) and (b >= d)) or ((c <= a) and (d >= b)):
            count1 += 1
        if ((a >= c) and (a <= d)) or ((b >= c) and (b <= d)) or ((c >= a) and (c <= b)) or ((d >= a) and (d <= b)):
            count2 += 1

print("Part One:")
print(str(count1) + "\n")
print("Part Two:")
print(str(count2) + "\n")
exit(0)
