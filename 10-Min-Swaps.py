#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    guys = []
    i = 0
    while i < len(arr):
        if(arr[i] != i+1):
            while (arr[i] != i+1): 
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
                guys.append((arr[i]-1, i))
                swaps += 1
                print(arr)
        i += 1
    print(guys)
    return swaps

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
