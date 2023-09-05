#!/usr/bin/python3

## Advent of Code 2022
## Day 5 - Supply Stacks
## https://adventofcode.com/2022/day/5

import os
import sys
from collections import deque

stacks = list()
for x in range (0,9):
    stacks.append(deque())
stackmap = list()
moves = list()

def doMove(num, source, target):
    for x in range(0, num):
        stacks[target - 1].append(stacks[source - 1].pop())

def printStacks():
    for s in stacks:
        txt = ""
        for i in s:
            txt += i
        print(txt)
    print()

with open("input05.txt") as f:
    mapread = False
    for line in f:
        line = line.rstrip()
        if mapread:
            moves.append(line)
        else:
            if line:
                stackmap.append(line)
            else:
                mapread = True

stackmap = stackmap[0:len(stackmap)-1]
for l in reversed(stackmap):
    i = 0
    row = ""
    for i in range(0, len(l)):
        if i == 1:
            if (l[i] != ' '):
                stacks[0].append(l[i])
            row += "1: " + l[i] + ", "
        elif (i - 1) % 4 == 0:
            col = int(((i - 1) / 4))
            if l[i] != ' ':
                stacks[col].append(l[i])
            row += str(int(((i - 1) / 4) + 1)) + ": " + l[i] + ", "

printStacks()

for move in moves:
    m = move.split(' ')
    doMove(int(m[1]), int(m[3]), int(m[5]))

tops = ""
for s in stacks:
    tops += s[len(s) - 1]

print("Part One:")
print(tops + "\n")
print("Part Two:")
exit(0)
