#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    
    def bin_search(key:int,arr:list)->int:
        low=0
        high=len(arr)-1
        mid=0
        
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]==key):
                return mid
            elif(arr[mid]<key)and(arr[mid-1]>key):
                return mid
            elif(arr[mid]>key)and(arr[mid+1]<key):
                return mid+1
            elif(arr[mid]<key):
                high=mid-1
            else:
                low=mid+1
        
        
    n=len(ranked)
    m=len(player)
    ranks=[0 for i in range(n)]
    ranks[0]=1
    result=list()
    for i in range(1,n):
        if(ranked[i]==ranked[i-1]):
            ranks[i]=ranks[i-1]
        else:
            ranks[i]=ranks[i-1]+1
    
    for score in player:
        if(score>ranked[0]):
            result.append(1)
        elif(score<ranked[n-1]):
            result.append(ranks[n-1]+1)
        else:
            index=bin_search(score,ranked)
            result.append(ranks[index])
        
    return result  
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
