#!/usr/bin/env python3

import sys
import timeit
"""
Advent of Code 2021 - Day 2
Addison Freeman
"""

# Part 1 & 2
# grab list from file and splitby newline
arr = open("./day3.txt","r").read().splitlines()

# get the sum of all x[0] in arr.length
lst = [ [ y[i] for y in arr] for i, x in enumerate(arr[0])]

def most_common_bit(i, arr):
    if( sum(1 if int(x) == 1 else 0 for x in arr[i]) > sum(1 if int(x) == 0 else 0 for x in arr[i]) ):
        return 1
    else:
        return 0

def least_common_bit(i, arr):
    if( sum(1 if int(x) == 1 else 0 for x in arr[i]) < sum(1 if int(x) == 0 else 0 for x in arr[i]) ):
        return 1
    else:
        return 0

most_common_lst = [ most_common_bit(i, lst) for i, x in enumerate(lst)]
least_common_lst = [ least_common_bit(i, lst) for i, x in enumerate(lst)]

print(most_common_lst)
print(least_common_lst)

most_common_as_decimal = int("".join([str(x) for x in most_common_lst]), 2)
least_common_as_decimal = int("".join([str(x) for x in least_common_lst]), 2)

print(most_common_as_decimal * least_common_as_decimal)