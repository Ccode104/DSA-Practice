#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N, start, result):
    # Write your code here
    
    if(X==0):
        #Success!! in making a combination
        result[0]+=1
    elif(X<0):
        #Invalid Combination
        result[0]+=0
    else:
        for i in range(start,int(X**(1/N)+1)):
            start=i
            powerSum(X-(i**N), N, start+1, result)
           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())
    
    result=[0]
    
    powerSum(X, N, 1, result)

    fptr.write(str(result[0]) + '\n')

    fptr.close()
