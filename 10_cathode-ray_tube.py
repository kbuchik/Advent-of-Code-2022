#!/usr/bin/python3

## Advent of Code 2022
## Day 10 - Cathode-Ray Tube
## https://adventofcode.com/2022/day/10

import math
import os
import sys

cycle = 0
register = 1
acc = 0
part1sum = 0

targetCycles = [20, 60, 100, 140, 180, 220]

CRT = list()

def incCycle(c=1):
    global cycle, register, part1sum
    cycle += c
    if cycle in targetCycles:
        part1sum += cycle * register
    drawPixel(pix=register, c=cycle)

def initCRT():
    global CRT
    for i in range(0, 6):
        row = list()
        for j in range(0, 40):
            row.append('.')
        CRT.append(row)

def drawPixel(pix=register, c=cycle):
    pos = (c % 240)
    row = math.floor(pos / 40)
    col = pos % 40
    pixframe = [((pix - 1) % 40), (pix % 40), ((pix + 1) % 40)]
    #print("Register: {0}; pixframe: {1}".format(register, str(pixframe)))
    if col in pixframe:
        CRT[row][col] = '#'

def drawCRT():
    row = ""
    for r in CRT:
        print(''.join(r))
    print()

initCRT()

with open("input10.txt") as f:
    for line in f:
        line = line.rstrip().split(' ')
        if acc != 0:
            incCycle()
            register += acc
            acc = 0
        incCycle()
        if line[0] == "addx":
            acc = int(line[1])
        #print("End of cycle {0}; instruction: {1}".format(cycle, ' '.join(line)))
        #drawCRT()

print("Part One:")
print(str(part1sum) + "\n")
print("Part Two:")
drawCRT()
exit(0)
