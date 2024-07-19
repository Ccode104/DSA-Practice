#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    n=len(arr)

    #Replace the first half of elements with "-"
    for i in range(n//2):
        arr[i][1]='-'
    
    sorted_list=[[] for i in range(n)]
    
    #Use Radix Sort
    for i in range(n):
        sorted_list[int(arr[i][0])].append(arr[i][1])

    #Convert to 1D and include the spaces as well    
    result=[]
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list[i])):
            result.append(sorted_list[i][j])
            result.append(" ")
    
    print("".join(result))      
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
