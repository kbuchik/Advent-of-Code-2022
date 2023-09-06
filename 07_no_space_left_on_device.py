#!/usr/bin/python3

## Advent of Code 2022
## Day 7 - No Space Left On Device
## https://adventofcode.com/2022/day/7

import os
import sys
from treelib import Node, Tree

dirtree = Tree()
cdir = "/"

# Accepts a list containing the result of an "ls" command, one file per list entry
def countDirSize(dirlist):
    size = 0
    for x in dirlist:
        f = x.split(' ')
        if x[0] == "dir":
            continue
        else:
            size += f[0]
    return size

def addFileNode(fline):
    fl = line.split(" ")
    if not dirtree.get_node(fl[1]):
        if fl[0] == "dir":
            dirtree.create_node(fl[1], fl[1], parent=cdir, data=0)
            print("Added dir node: " + fl[1])
        else:
            dirtree.create_node(fl[1], fl[1], parent=cdir, data=int(fl[0]))
            print("Added file node: " + fl[1] + " with size " + fl[0])

with open("input07.txt") as f:
    listMode = False
    dirtree.create_node("/", "/")
    for line in f:
        line = line.rstrip()
        if listMode:
            if line.startswith("$"):
                listMode = False
            else:
                addFileNode(line)
                continue
        if line == "$ cd /":
            continue
        elif line == "$ ls":
            listMode = True
        elif line == "$ cd ..":
            if cdir != "/":
                pdir = dirtree.parent(cdir).tag
                cdir = pdir
                print("Directory moved up to: " + cdir)
            continue
        elif line.startswith("$ cd"):
            entry = line.split(" ")
            cdir = entry[2]
            print("Directory changed in to: " + cdir)
        
#dirtree.show()
exit(0)

print("Part One:")

print("Part Two:")


exit(0)
