#!/usr/bin/python3

## Advent of Code 2022
## Day 3 - Rucksack Reorganization
## https://adventofcode.com/2022/day/3

import os
import sys

prios = dict()
for x in range(97, 123):
    prios[chr(x)] = x - 96
for x in range(65, 91):
    prios[chr(x)] = x - 38

total1 = 0
total2 = 0
badges = list()

with open("input03.txt") as f:
    triplet = list()
    for line in f:
        line = line.rstrip()
        midp = int(len(line) / 2)
        c1 = line[0:midp]
        c2 = line[midp:len(line)]
        #print("Rucksack:  " + c1 + " " + c2)
        for i in c1:
            if i in c2:
                total1 += prios[i]
                break
        if (len(triplet) == 3):
            for i in triplet[0]:
                if i in triplet[1] and i in triplet[2]:
                    if i not in badges:
                        badges.append(i)
                    break
            triplet.clear()
        else:
            triplet.append(line)
    for i in badges:
        total2 += prios[i]

print("Part One:")
print(str(total1) + "\n")
print("Part Two:")
print(str(total2) + "\n")
exit(0)
