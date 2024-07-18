#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    
    freq_of_rem=[0 for i in range(k)]
    for num in s:
        freq_of_rem[(num%k)]+=1
    print(freq_of_rem)
    result=0
    
    if(freq_of_rem[0]>=1):
        result+=1
    if(k%2==0):
        for i in range(1,(k//2)):
            result+=max(freq_of_rem[i],freq_of_rem[(k-i)])
        result+=min(1,freq_of_rem[k//2])
    else:
        for i in range(1,(k//2)+1):
            result+=max(freq_of_rem[i],freq_of_rem[(k-i)])
        
        
    print(result)
    return result 
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
