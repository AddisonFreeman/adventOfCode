#!/usr/bin/env python3

import sys

"""
Advent of Code 2021 - Day 2
Addison Freeman
"""

# Part 1 & 2
# grab list from file and splitby newline
arr = open("./2021_day2.txt","r").read().splitlines()
# split into command and value
tup = [ [''.join([j for j in arr[i] if not j.isdigit()]).strip(), int(''.join(filter(str.isdigit, arr[i])))]  for i,x in enumerate(arr) ]
# horizontal, vertical, aim
pos = [0,0,0]
def move(tup):
    for cmd,amt in tup:
        if(cmd == "forward"):
            pos[0] += amt
            pos[1] += pos[2] * amt
        elif(cmd == "up"):
            pos[2] -= amt
        elif(cmd == "down"):
            pos[2] += amt
    return pos[0] * pos[1]

res = move(tup)
print(res)