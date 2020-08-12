#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def countChars(seq: str) -> dict:
    """
    returns a map of character keys with values of how many times they occur
    in the string
    """
    d = defaultdict(lambda: 0)
    for c in seq:
        d[c] += 1
    return d

def computeDelta(a, b: dict) -> int:
    """
    Given 2 maps (map[letter] = count) return the diffence (delta) between these values
    """
    keys = set(a.keys()).union(set(b.keys())) 
    return sum([abs(a[k] - b[k]) for k in keys])

# Complete the makeAnagram function below.
def makeAnagram(a, b: str) -> int:
    dataA = countChars(a)
    dataB = countChars(b)
    return computeDelta(dataA, dataB)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

