#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    
    # dp[i] is the number of ways to get the amount 'j' 
    dp = [0 for i in range(n+1)]
    
    # The number of ways to get '0' is 1(choose none- base case)
    
    dp[0] = 1
    
    # The number of ways to get amount 'j' will be the 
    # sum of number of ways to get the amount 'j-c[i]' 
    # for each c[i] since 'c[i]+j-c[i]=j'
     
    for i in range(len(c)):
        for j in range(c[i], n+1):
            dp[j] += dp[(j-c[i])]
            
    return dp[n]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
