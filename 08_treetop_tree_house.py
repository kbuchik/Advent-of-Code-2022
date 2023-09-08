#!/usr/bin/python3

## Advent of Code 2022
## Day 8 - Treetop Tree House
## https://adventofcode.com/2022/day/8

import os
import sys

forest = list()
fWidth = 0
fLength = 0

def treeVisible(y, x):
    tree = forest[y][x]
    visibleNorth = True
    visibleSouth = True
    visibleEast = True
    visibleWest = True
    # check north
    for i in reversed(range(0, y)):
        if forest[i][x] >= tree:
            visibleNorth = False
            break
    if visibleNorth:
        return True
    # check south
    for i in range(y + 1, fLength):
        if forest[i][x] >= tree:
            visibleSouth = False
            break
    if visibleSouth:
        return True
    # check east
    for j in range(x + 1, fWidth):
        if forest[y][j] >= tree:
            visibleEast = False
            break
    if visibleEast:
        return True
    # check west
    for j in reversed(range(0, x)):
        if forest[y][j] >= tree:
            visibleWest = False
            break
    return (visibleNorth or visibleSouth or visibleEast or visibleWest)

def scenicScore(y, x):
    tree = forest[y][x]
    score = [0, 0, 0, 0]
    # score north
    for i in reversed(range(0, y)):
        score[0] += 1
        if forest[i][x] >= tree:
            break
    # score south
    for i in range(y + 1, fLength):
        score[1] += 1
        if forest[i][x] >= tree:
            break
    # score east
    for j in range(x + 1, fWidth):
        score[2] += 1
        if forest[y][j] >= tree:
            break
    # score west
    for j in reversed(range(0, x)):
        score[3] += 1
        if forest[y][j] >= tree:
            break
    return score[0] * score[1] * score[2] * score[3]

with open("input08.txt") as f:
    y = 0
    for line in f:
        line = line.rstrip()
        x = 0
        forest.append(list())
        for t in line:
            forest[y].append(t)
            x += 1
        fWidth = x
        y += 1
    fLength = y

visibleCount = 0
highScenicScore = 0

for i in range(0, fLength):
    line = ""
    for j in range(0, fWidth):
        if treeVisible(i, j):
            visibleCount += 1
        ss = scenicScore(i, j)
        if ss > highScenicScore:
            #print("New high scenic score of {0} found at tree {1},{2}".format(ss, i, j))
            highScenicScore = ss

print("Part One:")
print(str(visibleCount) + "\n")
print("Part Two:")
print(str(highScenicScore) + "\n")
exit(0)
