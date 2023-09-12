#!/usr/bin/python3

## Advent of Code 2022
## Day 11 - Supply Stacks
## https://adventofcode.com/2022/day/11

import os
import sys

debug = False

class Monkey:
    def __init__(self, items, oper, testValue, trueTarget, falseTarget):
        self.items = items
        self.oper = oper
        self.testValue = testValue
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
    
    @staticmethod
    def makeMonkey(descStr):
        sItems = list()
        sOper = None
        sTest = 1
        sTrue = -1
        sFalse = -1
        if debug:
            print("Building monkey with the following descString:")
            print(descStr)
        for line in descStr:
            line = line.strip()
            if line.startswith("Starting items"):
                iList = line.split(" ")[2:]
                for i in iList:
                    if i.endsWith(","):
                        i = i[:-1]
                    sItems.append(int(i))
            elif line.startswith("Operation"):
                iOps = line.split(" ")[1:]
                sOper = (lambda n: n)
                # I have no idea how to implement this lol
            elif line.startswith("Test"):
                sTest = int(line.split(" ")[-1:])
            elif line.startswith("If true"):
                sTrue = int(line.split(" ")[-1:])
            elif line.startswith("If false"):
                sFalse = int(line.split(" ")[-1:])
        return Monkey(sItems, sOper, sTest, sTrue, sFalse)
        
    def __str__(self):
        descStr = "\tStarting items: " + ", ".join(self.items)
        descStr = descStr[:-2] + "\n"
        descStr += "\tOperation: {0}\n".format(str(self.oper))
        descStr += f"\tTest: divisible by {self.testValue}\n"
        descStr += f"\t\tIf true: throw to monkey {self.trueTarget}\n"
        descStr += f"\t\tIf false: throw to monkey {self.falseTarget}\n"
        return descStr
    
    def giveItem(i):
        items.append(i)
    
    def doOper(n):
        return oper(n)
    
    def modTest(n):
        return (n % testValue) == 0

monkeys = dict()
rounds = 0
part1sum = 0

with open("input11.txt") as f:
    currMonkey = 0
    buildingMonkey = False
    monkeyDesc = ""
    for line in f:
        line = line.rstrip()
        if buildingMonkey:
            if len(line) == 0 or line.startswith("Monkey"):
                monkeys[currMonkey] = Monkey.makeMonkey(monkeyDesc)
                buildingMonkey = False
                monkeyDesc = ""
            else:
                monkeyDesc += line
        if line.startswith("Monkey"):
            buildingMonkey = True
            currMonkey = int(line.split(" ")[1][:-1])
            print("Building monkey " + str(currMonkey))

exit(0)

for key, value in monkeys.items():
    print(f"Monkey {key}:")
    print(str(value))

print("Part One:")
#print(tops1 + "\n")
#print("Part Two:")
#print(tops2 + "\n")
exit(0)
