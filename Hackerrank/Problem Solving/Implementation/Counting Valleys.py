#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    
    # Level
    count=0
    
    # Count of the number of times we cross zero level 
    zero_count=0
    
    # Number of valleys(between two 0s with all -ve levels)
    valleys=0
    
    for direction in path:
        
        # If we get a valley with valid boundary
        if(zero_count%2==0):
            
            # Two sea levels for each valley
            valleys+=zero_count//2
            
            # The sea level at end of current valley may start a new valley 
            zero_count=1
         
         # We cross sea level   
        if(count==0):
            zero_count+=1
        
        # We go UP
        if(direction=='U'):
            count+=1
        
        # We go DOWN
        else:
            count-=1
        
        # We are above sea level(no valley)
        if(count>0):
            zero_count=0
        
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
