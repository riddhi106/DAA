#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(s):
    return len(set(s))

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    results = []
    for i in range(1, n + 1):
        s = data[i]
        results.append(stringConstruction(s))
    
    for result in results:
        print(result)
