#!/usr/bin/python3

## Advent of Code 2022
## Day 11 - Monkey in the Middle
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
    def makeMonkey(descLines):
        sItems = list()
        sOper = "old"
        sTest = 1
        sTrue = -1
        sFalse = -1
        for line in descLines:
            line = line.strip()
            if debug:
                print("\t" + line)
            if line.startswith("Starting items"):
                iList = line[16:].split(", ")
                for i in iList:
                    sItems.append(int(i))
            elif line.startswith("Operation"):
                sOper = line[17:]
            elif line.startswith("Test"):
                sTest = int(line.split(" ")[-1])
            elif line.startswith("If true"):
                sTrue = int(line.split(" ")[-1])
            elif line.startswith("If false"):
                sFalse = int(line.split(" ")[-1])
        return Monkey(sItems, sOper, sTest, sTrue, sFalse)
        
    def __str__(self):
        descStr = "\tStarting items: {0}\n".format(", ".join(map((lambda i: str(i)), self.items)))
        descStr += "\tOperation: new = {0}\n".format(self.oper)
        descStr += f"\tTest: divisible by {self.testValue}\n"
        descStr += f"\t\tIf true: throw to monkey {self.trueTarget}\n"
        descStr += f"\t\tIf false: throw to monkey {self.falseTarget}\n"
        return descStr
    
    def giveItem(i):
        items.append(i)
    
    def doOper(old):
        return eval(oper)
    
    def modTest(n):
        return (n % testValue) == 0

monkeys = dict()
rounds = 0
part1sum = 0

with open("input11.txt") as f:
    currMonkey = 0
    buildingMonkey = False
    monkeyDesc = list()
    for line in f:
        line = line.rstrip()
        if buildingMonkey:
            if len(line) == 0 or line.startswith("Monkey"):
                monkeys[currMonkey] = Monkey.makeMonkey(monkeyDesc)
                buildingMonkey = False
                monkeyDesc = list()
            else:
                monkeyDesc.append(line)
        if line.startswith("Monkey"):
            buildingMonkey = True
            currMonkey = int(line.split(" ")[1][:-1])
    if buildingMonkey:
        monkeys[currMonkey] = Monkey.makeMonkey(monkeyDesc)

for key, value in monkeys.items():
    print(f"Monkey {key}:")
    print(str(value))

print("Part One:")

#print("Part Two:")

exit(0)
