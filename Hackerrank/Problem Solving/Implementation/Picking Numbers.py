#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    def check_diff(elem,minimum,maximum):
        
        
        result=True
        
        if(abs(maximum-elem)>1)or(abs(minimum-elem)>1):
            result=False
        return result
        
    n=len(a)
    max_len=0
   
    for i in range(n):
        minimum=maximum=a[i]
        length=1
        for j in range(n):
            if(i!=j)and(check_diff(a[j],minimum,maximum)==False):
                pass
            elif(i!=j):
                if(minimum>a[j]):
                    minimum=a[j]
                if(maximum<a[j]):
                    maximum=a[j]
                length+=1
           
        if(max_len<length):
            max_len=length
    return max_len
                 
       #Time Complexity:O(n^2)
       #Space Complexity:O(1)
       
       #It can be solved in O(n) by using Hash Table but Space will be O(max(a)-min(a)+1) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
