#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sorted_array = sorted(arr)
#    print(sorted_array)
    arr_len = len(sorted_array)
#    print(arr_len)
    sum_min = 0
    sum_max = 0
    for i in range(0,arr_len-1):
        sum_min+=sorted_array[i]
#    print(sum_min)
    for j in range(arr_len-1,0,-1):
        sum_max+=sorted_array[j]
#    print(sum_max)
    print(sum_min, sum_max)

    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
