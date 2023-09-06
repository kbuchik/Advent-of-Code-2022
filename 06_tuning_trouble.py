#!/usr/bin/python3

## Advent of Code 2022
## Day 4 - Camp Cleanup
## https://adventofcode.com/2022/day/4

import os
import sys
from collections import deque

headerFrame = deque()
headerFrameSize = 4
messageFrame = deque()
messageFrameSize = 14
headerPos = 0
messagePos = 0

# returns True if frame (fr) contains no repeated characters
def checkFrame(fr):
    for i in range(0, len(fr) - 1):
        for j in range(i + 1, len(fr)):
            if fr[i] == fr[j]:
                return False
    return True

with open("input06.txt") as f:
    signal = f.readline()
    pos = 0
    for c in signal:
        pos += 1
        if len(headerFrame) < headerFrameSize:
            headerFrame.append(c)
        else:
            headerFrame.popleft()
            headerFrame.append(c)
            if checkFrame(headerFrame) and headerPos == 0:
                headerPos = pos
        if len(messageFrame) < messageFrameSize:
            messageFrame.append(c)
        else:
            messageFrame.popleft()
            messageFrame.append(c)
            if checkFrame(messageFrame) and messagePos == 0:
                messagePos = pos

print("Part One:")
print(str(headerPos))
print("Part Two:")
print(str(messagePos))

exit(0)
