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

# Part 1

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

# print(count)

# 
# Part 2
# 

one = [ [x]  for i,x in enumerate(list_int[:-1]) ]
tup = [ [x, list_int[i+1] ] for i,x in enumerate(list_int[:-1]) ]
trip = [ [x, list_int[i+1], list_int[i+2] ] for i,x in enumerate(list_int[:-2]) ]
quad = [ [x, list_int[i+1], list_int[i+2], list_int[i+3] ] for i,x in enumerate(list_int[:-3]) ]

def compare(arr):
    count = 0
    for i in enumerate(arr):
        idx = i[0]
        if(idx > len(arr) - 2):
            break
        if (sum(arr[idx+1]) > sum(arr[idx])):
            count += 1
    print(count)

compare(one)
compare(tup)
compare(trip)
compare(quad)