#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def unboundedKnapsack(k, arr):
    dp = [0] * (k + 1)
    for i in range(1, k + 1):
        for num in arr:
            if num <= i:
                dp[i] = max(dp[i], dp[i - num] + num)
    return dp[k]

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        arr = list(map(int, data[index + 2:index + 2 + n]))
        index += 2 + n
        result = unboundedKnapsack(k, arr)
        results.append(result)
    
    for res in results:
        print(res)
