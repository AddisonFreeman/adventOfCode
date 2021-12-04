#!/usr/bin/env python3

import sys
import timeit
"""
Advent of Code 2021 - Day 2
Addison Freeman
"""

# Part 1 & 2
# grab list from file and splitby newline
raw_input = open("./day3.txt","r").read().splitlines()

# make a 2d array of each row by bit position
lst = [ [ y[i] for y in raw_input] for i, x in enumerate(raw_input[0])]
# count the number of bits in array row given the index
def count_in_array(arr, bit):
    return sum(1 if int(x) == int(bit) else 0 for x in arr)
# bool of which bit is more common in array row given the index  
def compare_bits(i, arr, op):
    count_ones = count_in_array(arr[i], 1)
    count_zeros = count_in_array(arr[i], 0)
    # print(count_ones, count_zeros)
    if(op == "gt"):
        return count_ones > count_zeros
    elif(op == "lt"):
        return count_ones < count_zeros
#  find most common bit in row of array given the index
def most_common_bit(i, arr):
    if( compare_bits(i, arr, "gt") ):
        return 1
    else:
        return 0
#  find least common bit in row of array given the index
def least_common_bit(i, arr):
    if( compare_bits(i, arr, "lt") ):
        return 1
    else:
        return 0
# generate a list of most and least common bits for each row (note: will be inverse)
most_common_lst = [ most_common_bit(i, lst) for i, x in enumerate(lst)]
least_common_lst = [ least_common_bit(i, lst) for i, x in enumerate(lst)]

# print(most_common_lst)
# print(least_common_lst)
# convert list of most/least common bits to decimal
most_common_as_decimal = int("".join([str(x) for x in most_common_lst]), 2)
least_common_as_decimal = int("".join([str(x) for x in least_common_lst]), 2)

print("part 1 answer", most_common_as_decimal * least_common_as_decimal)

oxy_index = []
co2_index = []

def indices_where(arr, bit):
    return [ i if int(x) == int(bit) else '' for i,x in enumerate(arr) ]

# filter out most/least common bits from row given index
def filter_bits(arr, op):
    count_ones = count_in_array(arr, 1)
    count_zeros = count_in_array(arr, 0)
    
    # most common bit case
    if(op == "gt"):
        if(count_ones > count_zeros):
            print("more 1 than 0")
            # return array of index for numbers that are 1
            return indices_where(arr, 1)
        else:
            print("not more 1 than 0")
            # return array of index for numbers that are 0
            return indices_where(arr, 0)
    elif(op == "lt"):
        if(count_ones < count_zeros):
            print("less 1 than 0")
            # return array of index for numbers that are 1
            return indices_where(arr, 1)
        else:
            print("not less 1 than 0")
            # return array of index for numbers that are 0
            return indices_where(arr, 0)

# generate list of indices to remove from
valid_numbers_gt = range(len(lst[0]))
valid_numbers_lt = range(len(lst[0]))

filter_keep_ones = [ filter_bits(lst[i], "gt") for i, x in enumerate(lst)]
filter_keep_zeros = [ filter_bits(lst[i], "lt") for i, x in enumerate(lst)]

# first_row_down = lst[0]
# count_ones = count_in_array(first_row_down, 1)
# count_zeros = count_in_array(first_row_down, 0)
# print(count_ones, count_zeros)

# ret = filter_bits(first_row_down, "gt")
print(filter_keep_ones[-1])

