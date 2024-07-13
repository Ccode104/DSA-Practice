#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    
    if(n%2!=0):
        if(p%2==0):
            #even
            if((p//2)<((n-p-1)//2)):
                minimum_pages=p//2
            else:
                minimum_pages=(n-p-1)//2
        else:
            if(((n-p)//2)<((p-1)//2)):
                minimum_pages=(n-p)//2
            else:
                minimum_pages=(p-1)//2
    else:
        if(p%2==0):
            #even
            if((p//2)<((n-p)//2)):
                minimum_pages=p//2
            else:
                minimum_pages=(n-p)//2
        else:
            if(((n-p+1)//2)<((p-1)//2)):
                minimum_pages=((n-p+1)//2)
            else:
                minimum_pages=(p-1)//2
        
    return minimum_pages
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
