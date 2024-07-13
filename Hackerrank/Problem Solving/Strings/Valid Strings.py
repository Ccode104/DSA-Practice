#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    freq=[0 for i in range(26)]
    
    for character in s:
        freq[ord(character)-ord('a')]+=1
    print(freq)
    only_freq=list()
    for f in freq:
        if(f!=0):
            only_freq.append(f)
    print(only_freq)
    max_freq=max(only_freq)
    min_freq=min(only_freq) 
    
    if(max_freq==min_freq):
         ret_val="YES"
    elif(only_freq.count(max_freq)==1)and(max_freq-min_freq==1):
        ret_val="YES"
    elif(only_freq.count(min_freq)==1)and(min_freq==1):
        only_freq.remove(min_freq)
        if(max_freq==min(only_freq)):
            ret_val="YES"
        else:
            ret_val="NO"     
    else:
         ret_val="NO"
    return ret_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()