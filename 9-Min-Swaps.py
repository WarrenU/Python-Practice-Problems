#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = [] #  List of tuples
    N = len(arr)
    i = 0
    x = 0
    while x < 13 and i < N-1:
      target = arr[i] 
      try:
        minVal, minInd = getMin(arr[i+1:])
        minInd += 1
      except IndexError:
        import pdb; pdb.set_trace()
      print(f"target: {target} minVal: {minVal} arr: {arr}")
      if i < minInd and target > minVal:
        swaps.append((i, minInd))
        arr[i], arr[minInd] = arr[minInd], arr[i]
      else:
        i += 1
      x += 1


    print("\n---------")
    print(arr)
    print(swaps)
    return len(swaps)

def getMin(arr) -> (int, int):
  index = 0
  value = arr[0]
  for i in range(len(arr)):
    if arr[i] < value:
      value = arr[i]
      index = i
  return value, index

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
