#Reference:https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    y=len(arr[0]) #Cols
    x=len(arr)     #Rows
    sum=0
    max=-100   #Stores max sum
    for i in range(1,x-1):
        for j in range(1,y-1):
            #Calulate sum of the hourglass centered at (i,j)
            sum=arr[i][j]
            for k in range(j-1,j+2):
                sum=sum+arr[i-1][k]+arr[i+1][k]
            if(max<sum):
               max=sum
    return max
            
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
