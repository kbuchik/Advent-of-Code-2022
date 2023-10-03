#!/usr/bin/python3

## Advent of Code 2022
## Day 11 - Monkey in the Middle
## https://adventofcode.com/2022/day/11

import copy
import math
import os
import sys

debug = True
monkeyDebug = False
worryDivision = True
monkeys = dict()
monkeys2 = dict()
dropsTable = dict()
rounds = 0
TOTAL_ROUNDS = 20
WORRY_DIVISOR = 3

class Monkey:
    def __init__(self, items, oper, testValue, trueTarget, falseTarget):
        self.items = items
        self.oper = oper
        self.testValue = testValue
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
        self.inspectCount = 0
    
    @staticmethod
    def makeMonkey(descLines):
        sItems = list()
        sOper = "old"
        sTest = 1
        sTrue = -1
        sFalse = -1
        for line in descLines:
            line = line.strip()
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
        descStr = "\tStarting items: {0}\n".format(showItems())
        descStr += "\tOperation: new = {0}\n".format(self.oper)
        descStr += f"\tTest: divisible by {self.testValue}\n"
        descStr += f"\t\tIf true: throw to monkey {self.trueTarget}\n"
        descStr += f"\t\tIf false: throw to monkey {self.falseTarget}\n"
        return descStr
    
    def giveItem(self, i):
        self.items.append(i)
    
    def doOper(self, old):
        return eval(self.oper)
    
    def modTest(self, n):
        return (n % self.testValue) == 0
    
    def showItems(self):
        if len(self.items) > 0:
            return ", ".join(map((lambda i: str(i)), self.items))
        else:
            return ""
    
    # for ease of processing, turn() will return a dict of items where the key is the monkey to give it to and the value is the "worry level"
    def turn(self):
        global dropsTable
        cleanup = list()
        if monkeyDebug and len(self.items) == 0:
            print("\tMonkey's inventory is empty and so it takes no action.")
        for i in self.items:
            if monkeyDebug:
                print(f"\tMonkey inspects an item with a worry level of {i}.")
            n = self.doOper(i)
            if monkeyDebug:
                print(f"\t\tAfter operation \"{self.oper}\" worry level is now {n}.")
            if worryDivision:
                n = math.floor(n / WORRY_DIVISOR)
            if monkeyDebug:
                print(f"\t\tWorry level is divided by 3 to {n}.")
            if self.modTest(n):
                if monkeyDebug:
                    print(f"\t\tCurrent worry level is divisible by {self.testValue}.")
                    print(f"\t\tItem with worry level {n} is thrown to monkey {self.trueTarget}.")
                dropsTable[self.trueTarget].append(n)
            else:
                if monkeyDebug:
                    print(f"\t\tCurrent worry level is not divisible by {self.testValue}.")
                    print(f"\t\tItem with worry level {n} is thrown to monkey {self.falseTarget}.")
                dropsTable[self.falseTarget].append(n)
            cleanup.append(i)
            self.inspectCount += 1
        for i in cleanup:
            self.items.remove(i)

def printMonkeyInventories():
    print(f"After round {rounds}, the monkeys are holding items with these worry levels:")
    for key, monkey in monkeys.items():
        print(f"Monkey {key}: " + monkey.showItems())
    print()

def setupDropsTable():
    global dropsTable
    dropsTable = dict()
    for m in monkeys:
        dropsTable[m] = list()

def monkeyBusinessRound():
    global dropsTable
    for key, monkey in monkeys.items():
        #print(f"Monkey {key}:")
        #print(str(monkey))
        if monkeyDebug:
            print(f"Monkey {key}:")
        monkey.turn()
        for target, drops in dropsTable.items():
            for i in drops:
                monkeys[target].giveItem(i)
        setupDropsTable()
    if monkeyDebug:
        print()

with open("input11.txt") as f:
    currMonkey = 0
    buildingMonkey = False
    monkeyDesc = list()
    # build da monkeys
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
    setupDropsTable()

monkeys2 = copy.deepcopy(monkeys)

if debug:
    printMonkeyInventories()

# monkey bidness part 1
for r in range(0, TOTAL_ROUNDS):
    rounds += 1
    monkeyBusinessRound()
    if debug:
        printMonkeyInventories()

iCounts = list()

for key, monkey in monkeys.items():
    count = monkey.inspectCount
    print(f"Monkey {key} inspected items {count} times")
    iCounts.append(count)
print()

iCounts = list(reversed(sorted(iCounts)))

part1sum = iCounts[0] * iCounts[1]
exit(0)

# monkey bidness part 2
worryDivision = False
TOTAL_ROUNDS = 10000
monkeys = monkeys2
rounds = 0
setupDropsTable()
for r in range(0, TOTAL_ROUNDS):
    rounds += 1
    monkeyBusinessRound()
    if debug:
        printMonkeyInventories()

iCounts = list()

for key, monkey in monkeys.items():
    count = monkey.inspectCount
    print(f"Monkey {key} inspected items {count} times")
    iCounts.append(count)
print()

iCounts = list(reversed(sorted(iCounts)))

part2sum = iCounts[0] * iCounts[1]

print("Part One:")
print(str(part1sum))
print("Part Two:")
print(str(part2sum))

exit(0)
