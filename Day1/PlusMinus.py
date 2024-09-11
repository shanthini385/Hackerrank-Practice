#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    count_positive = 0
    count_zero = 0
    count_neg = 0
    array_len=len(arr)
    for i in arr:
        if i > 0:
            count_positive+=1
        elif i == 0:
            count_zero+=1
        else:
            count_neg+=1
    pos=float(count_positive/array_len)
    zer=float(count_zero/array_len)
    neg=float(count_neg/array_len)
    print("{:.6f}".format(round(pos, 6)))
    print("{:.6f}".format(round(zer, 6)))
    print("{:.6f}".format(round(neg, 6)))
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
