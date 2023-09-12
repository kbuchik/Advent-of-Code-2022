#!/usr/bin/python3

## Advent of Code 2022
## Day 10 - Cathode-Ray Tube
## https://adventofcode.com/2022/day/10

import math
import os
import sys
from collections import deque

cycle = 0
register = 1
acc = 0
instructions = deque()
CRT = list()

part1sum = 0
targetCycles = [20, 60, 100, 140, 180, 220]
debug = False

def cycleOps():
    global cycle, register, part1sum
    if cycle in targetCycles:
        part1sum += cycle * register
    drawPixel(pix=register, cyc=cycle)

def initCRT():
    global CRT
    for i in range(0, 6):
        row = list()
        for j in range(0, 40):
            row.append(' ')
        CRT.append(row)

def drawCRT():
    row = ""
    for r in CRT:
        print(''.join(r))
    print()

def drawPixel(pix=register, cyc=cycle):
    pos = (cyc % 240)
    row = math.floor(pos / 40)
    col = (pos % 40) - 1
    pixframe = [((pix - 1) % 40), (pix % 40), ((pix + 1) % 40)]
    p = '.'
    if col in pixframe:
        p = '#'
    CRT[row][col] = p
    if debug:
        print("During cycle {0}: CRT draws pixel {1} in position {2}".format(cyc, p, col))
        print("Current CRT row: " + ''.join(CRT[row]))

initCRT()

with open("input10.txt") as f:
    for line in f:
        instructions.append(line.rstrip())

while len(instructions) > 0:
    cycle += 1
    if acc != 0:
        cycleOps()
        register += acc
        if debug:
            print("End of cycle {0}: finish executing addx {1} (Register X is now {2})".format(cycle, acc, register))
        acc = 0
    else:
        ins = instructions.popleft().split(' ')
        if debug:
            print("Start cycle {0}: begin executing {1}".format(cycle, ' '.join(ins)))
        if ins[0] == "addx":
            acc = int(ins[1])
        cycleOps()
    print()

print("Part One:")
print(str(part1sum) + "\n")
print("Part Two:")
drawCRT()
exit(0)
