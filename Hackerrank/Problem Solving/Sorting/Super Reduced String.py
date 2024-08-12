#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# IDEA : 
# Insert the character in stack if not equal to the one at the top of the stack
# else we pop out from the stack (similar to mechanism followed in paranthesis match)

def superReducedString(s):
    # Write your code here
    
    n=len(s)
    
    stack=[s[0]]
    top=0
    
    for character in s[1:]:
        if(top>=0):
            if(stack[top]==character):
                stack.pop(top)
                top-=1
            else:
                stack.append(character)
                top+=1
        else:
            stack.append(character)
            top+=1
    
    if(top<0):
        return 'Empty String'
    else:       
        return "".join(stack)
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
