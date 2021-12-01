#!/usr/bin/env python3

import sys

"""
Advent of Code 2020 - Day 1
R3cUr$10N R3M!X
"""

expenses_file = open("./day1.txt","r")
expenses_sorted = expenses_file.read().splitlines()

expenses_sorted.sort()

def find_2020(expenses_sorted, head, last):
    print(head, last)
    # provide an exit case for if recursion is called for invalid inputs
    if(head > len(expenses_sorted) or last < 1):
        return False
    # sum the result for this iteration
    res = int(expenses_sorted[head]) + int(expenses_sorted[last])
    print(expenses_sorted[head], expenses_sorted[last], res)
    # compare winning condition
    if(res == 2020):
        print("You WIN!", head, last, res)
        return
    # if larger than 2020, move last back by 1 and recurse
    elif(res > 2020):
        find_2020(expenses_sorted, head, last-1)
    # if smaller than 2020 move head forward by 1 and recurse
    elif(res < 2020):
        find_2020(expenses_sorted, head+1, last)
        
# call the defined method
find_2020(expenses_sorted,0,len(expenses_sorted)-1) 