#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    # Write your code here
    
    #Sort the array
    x.sort()
    
    n=len(x)
    
    #Number of transmitters
    count=0
    
    i=0
    
    while(i<n):
        
        #Find the ideal centre which will cover the ith element
        loc=x[i]+k
        
        #Search if it exists or less than it exists
        while(i<n)and(x[i]<=loc):
            i+=1
        
        #Place the transmitter
        i-=1
        count+=1
        
        #Go to the point just out of its range
        loc=x[i]+k
        
        while(i<n)and(x[i]<=loc):
            i+=1
            
    return count        
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
