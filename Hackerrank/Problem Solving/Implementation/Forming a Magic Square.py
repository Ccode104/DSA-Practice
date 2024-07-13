#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(matrix):
    # Write your code here
    
    #8 possible magic squares(3X3)(In 1D format)
    #The pattern remains same but is rotated or mirrored to get 8
    magic_squares=[[8,1,6,3,5,7,4,9,2],[6,1,8,7,5,3,2,9,4],[4,3,8,9,5,1,2,7,6],[2,7,6,9,5,1,4,3,8],[2,9,4,7,5,3,6,1,8],[4,9,2,3,5,7,8,1,6],[6,7,2,1,5,9,8,3,4],[8,3,4,1,5,9,6,7,2]]
    
    #Convert the matrix into 1D(Just for ease of writing)
    s=[]
    for i in range(3):
        for j in range(3):
            s.append(matrix[i][j])
            
    #The minimum cost is defined by the minimum abs.diff between elements
    #of Magic Square and given matrix 
    minimum_diff=sys.maxsize
    
    #Getting min. cost
    for m_sq in magic_squares:
        diff=0
        for i,j in zip(s,m_sq):
            diff+=abs(i-j)
        minimum_diff=min(minimum_diff,diff)
             
    return minimum_diff
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
