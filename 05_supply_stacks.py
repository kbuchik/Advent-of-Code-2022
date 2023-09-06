#!/usr/bin/python3

## Advent of Code 2022
## Day 5 - Supply Stacks
## https://adventofcode.com/2022/day/5

import copy
import os
import sys
from collections import deque

stacks = list()
bulkStacks = list()
for x in range (0,9):
    stacks.append(deque())
stackmap = list()
moves = list()

def doMove(num, source, target):
    for x in range(0, num):
        stacks[target - 1].append(stacks[source - 1].pop())

def doBulkMove(num, source, target):
    tmp = list()
    for x in range(0, num):
        tmp.append(bulkStacks[source - 1].pop())
    for y in reversed(tmp):
        bulkStacks[target - 1].append(y)

def printStacks(stx):
    for s in stx:
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

bulkStacks = copy.deepcopy(stacks)

for move in moves:
    m = move.split(' ')
    doMove(int(m[1]), int(m[3]), int(m[5]))
    doBulkMove(int(m[1]), int(m[3]), int(m[5]))


tops1 = ""
tops2 = ""
for s in stacks:
    tops1 += s[len(s) - 1]
for s in bulkStacks:
    tops2 += s[len(s) - 1]

print("Part One:")
print(tops1 + "\n")
print("Part Two:")
print(tops2 + "\n")
exit(0)
