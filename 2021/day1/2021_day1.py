#!/usr/bin/env python3

import sys
# importing functools for reduce()
import functools
# importing itertools for accumulate()
import itertools

"""
Advent of Code 2021 - Day 1
Addison Freeman
"""

# grab list from file and splitby newline
arr = open("./2021_day1.txt","r").read().splitlines()
# ensure list<int>, call list() to execute map() on object
list_int = list(map(int, arr))
# keep track of depth increase
count = 0
for i in enumerate(list_int):
    idx = i[0]
    val = i[1]
    if(idx > len(list_int)-2):
        break
    if (list_int[idx+1] > list_int[idx]):
         count += 1

print(count)

