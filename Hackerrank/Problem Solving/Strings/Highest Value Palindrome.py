#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    
    no_of_op=0
    s=list(s)
    index_mod=[0 for i in range(n)]
    for i in range(n):
        if(s[i]!=s[n-i-1]):
            no_of_op+=1
            index_mod[i]=1
            s[i]=s[n-1-i]=max(s[i],s[n-1-i])
    if(no_of_op>k):
        #Cannot obtain a palindrome
        return '-1'
    elif(no_of_op==k):
        #Can barely make a palindrome
        return "".join(s)
    else:
        #Fill it with 9s 
        i=0
        while(no_of_op<k)and(i<n):
            if(s[i]!='9'):
                if(index_mod[i]==1)or(i==n-1-i):
                    no_of_op+=1
                else:
                    no_of_op+=2
                if(no_of_op>k):
                    no_of_op-=2
                else:
                    s[i]=s[n-i-1]='9'
                        
            i+=1
        return "".join(s)
        
        
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
