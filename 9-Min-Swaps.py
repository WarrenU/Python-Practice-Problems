#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = [] #  List of tuples
    ans = 0
    N = len(arr)
    i = 0

    while i < N-1:
      curr = arr[i]
      m, index = getMinLeft(arr[i:])
      if curr > m:
        arr[i], arr[index+i] = arr[index+i], arr[i]
        swaps.append((i, index+i))
        ans += 1
        i -= 1
      i += 1
    return ans

def getMinLeft(arr) -> (int, int):
  """
  Get integer that needs to go left, from the starting Index.
  (int, int) : Value, Index
  """
  res = (arr[0], 0)
  for i in range(len(arr)):
    try:
      if arr[i] < arr[i-1] and arr[i] < res[0]:
        res = (arr[i], i)
    except IndexError:
      print("first element does not have a previous element to check")
  return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)

    fptr.write(str(res) + '\n')

    fptr.close()
