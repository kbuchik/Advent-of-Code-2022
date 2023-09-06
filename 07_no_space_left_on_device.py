#!/usr/bin/python3

## Advent of Code 2022
## Day 7 - No Space Left On Device
## https://adventofcode.com/2022/day/7

import os
import sys
from treelib import Node, Tree

cdir = "/"
dirtree = Tree()
dirsizes = dict()
maxSize = 100000
sizeTotal = 0
dupe_correct = 1

# Recursive function to the count the size of a directory and all children
def calcDirSize(directory):
    global sizeCount
    size = 0
    contents = dirtree.children(directory)
    for n in contents:
        if n.data:
            size += n.data
        if len(dirtree.children(n.tag)) > 0:
            size += calcDirSize(n.tag)
    if size > 0 and size <= maxSize:
        dirsizes[directory] = size
    return size

# Add the file represented by the given ls listing line (fline) to the tree, with cdir as parent
def addFileNode(fline):
    global dupe_correct
    fl = line.split(" ")
    name = fl[1]
    if dirtree.get_node(name):
        if dirtree.parent(name).tag == cdir:
            print("Actual duplicate add detected: " + fline)
            return
        else:
            name = name + "_" + str(dupe_correct)
            dupe_correct += 1
    if fl[0] == "dir":
        dirtree.create_node(name, name, parent=cdir)
    else:
        dirtree.create_node(name, name, parent=cdir, data=int(fl[0]))

# Print out tree structure for the given directory
def printDirListing(query):
    fnode = dirtree.get_node(query)
    if not fnode:
        print("No file or directory with name \"" + query + "\" exists in tree")
    else:
        print(dirListing(query))


# Get a string representing the tree structure of the given directory
def dirListing(query, treeStr="", tabLevel=0):
    fnode = dirtree.get_node(query)
    if not fnode:
        return treeStr
    treeStr += "\t" * tabLevel
    if fnode.data:
        return treeStr + "- {0} (file, size={1})".format(fnode.tag, str(fnode.data))
    else:
        contents = dirtree.children(fnode.tag)
        treeStr += "+ {0} (dir)".format(fnode.tag)
        for i in contents:
            treeStr += "\n"
            treeStr = dirListing(i.tag, treeStr=treeStr, tabLevel=tabLevel+1)
        return treeStr

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
                cdir = dirtree.parent(cdir).tag
            continue
        elif line.startswith("$ cd"):
            entry = line.split(" ")
            cdir = entry[2]
        
printDirListing("/")
exit(0)
dirtreeSize = calcDirSize("/")
print("All directories with size < " + str(maxSize))
for dirname,size in dirsizes.items():
    print(dirname + ": " + str(size))
    sizeTotal += size
print()

print("Part One:")
print(str(sizeTotal) + "\n")
#print("Part Two:")

exit(0)
