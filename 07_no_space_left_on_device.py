#!/usr/bin/python3

## Advent of Code 2022
## Day 7 - No Space Left On Device
## https://adventofcode.com/2022/day/7

import os
import sys
from treelib import Node, Tree

currNode = None
dirtree = Tree()
dirsizes = dict()
sizeTotal = 0
tabstr = "    "
dir_id = 1
file_id = 1

MAX_SIZE = 100000

# Recursive function to the count the size of a directory (identifier, not tag/name) and all children
def calcDirSize(directory):
    global sizeTotal, dirsizes
    dirNode = dirtree.get_node(directory)
    if not dirNode or dirNode.data:
        print("Error: calcDirSize() couldn't find directory with id: " + directory)
    size = 0
    contents = dirtree.children(directory)
    for n in contents:
        if n.data:
            size += n.data
        if len(dirtree.children(n.identifier)) > 0:
            size += calcDirSize(n.identifier)
    if size <= MAX_SIZE:
        dirkey = dirNode.tag + "|" + dirNode.identifier
        dirsizes[dirkey] = size
        sizeTotal += size
    return size

# Add the file represented by the given ls listing line (fline) to the tree, assuming currNode to be the parent
def addFileNode(fline):
    global dir_id, file_id, currNode
    fl = line.split(" ")
    if fl[0] == "dir":
        dirtree.create_node(tag=fl[1], identifier="dir_" + str(dir_id), parent=currNode.identifier)
        dir_id += 1
    else:
        dirtree.create_node(tag=fl[1], identifier="file_" + str(file_id), parent=currNode.identifier, data=int(fl[0]))
        file_id += 1
 
# Print out tree structure for the given directory
def printDirListing(query, dirSizes=False):
    fnode = dirtree.get_node(query)
    if not fnode:
        print("No file or directory with id \"" + query + "\" exists in tree")
    else:
        print(dirListing(query, dirSizes=dirSizes))


# Get a string representing the tree structure of the given directory
def dirListing(query, treeStr="", tabLevel=0, dirSizes=False):
    fnode = dirtree.get_node(query)
    if not fnode:
        return treeStr
    treeStr += tabstr * tabLevel
    if fnode.data:
        fline = "- {0} (file, size={1})".format(fnode.tag, str(fnode.data))
        return treeStr + fline
    else:
        contents = dirtree.children(fnode.identifier)
        fline = "+ {0} (dir".format(fnode.tag)
        if dirSizes:
            fline += ", size=" + str(calcDirSize(fnode.identifier))
        fline += ")"
        treeStr += fline
        for i in contents:
            treeStr += "\n"
            treeStr = dirListing(i.identifier, treeStr=treeStr, tabLevel=tabLevel+1, dirSizes=dirSizes)
        return treeStr

with open("input07.txt") as f:
    listMode = False
    dirtree.create_node(tag="/", identifier="dir_0")
    for line in f:
        line = line.rstrip()
        if listMode:
            if line.startswith("$"):
                listMode = False
            else:
                addFileNode(line)
                continue
        if line == "$ cd /":
            currNode = dirtree.get_node("dir_0")
            continue
        elif line == "$ ls":
            listMode = True
        elif line == "$ cd ..":
            if currNode.identifier != "dir_0":
                currNode = dirtree.parent(currNode.identifier)
            continue
        elif line.startswith("$ cd"):
            entry = line.split(" ")
            dirlist = dirtree.children(currNode.identifier)
            for fl in dirlist:
                if fl.tag == entry[2] and not fl.data:
                    currNode = fl
 
#printDirListing("dir_0", dirSizes=True)
#exit(0)
sizeTotal = 0
dirtreeSize = calcDirSize("dir_0")
#print("Total filesystem size: " + str(dirtreeSize))

'''
print("All directories with size < " + str(maxSize))
for dirname,size in dirsizes.items():
    print(dirname + ": " + str(size))
print()
'''

print("Part One:")
print(str(sizeTotal) + "\n")
#print("Part Two:")

exit(0)
