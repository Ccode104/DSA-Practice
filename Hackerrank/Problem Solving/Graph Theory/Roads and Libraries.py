!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

#Here we use the "Divide and Conquer" approach 
#to solve the subproblem for each disconnected component
def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    
    #To store the graph
    adjacency_list=[[]for i in range(n+1)]
    
    #Fill in the adjacency list
    for x,y in cities:
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)
    
    #The cost reqd
    total_cost=0
    
    #Tells if a city has been visited or not
    visited=[False for i in range(n+1)]
    
    #Depth First Search
    def dfs(u,adjacency_list,visited):
        visited[u]=True
        
        #Number of visited till now
        n_cities=1
        for v in adjacency_list[u]:
            if(visited[v]==False):
                n_cities+=dfs(v,adjacency_list,visited)
        
        return n_cities
    
    for u in range(1,n+1):
        if(visited[u]==False):
            
            #Place a library in city 'v' and bulid the roads to the remaining cities
            #excluding cylces(min spanning tree due to equal weight edges) 
            
            n_cities=dfs(u,adjacency_list,visited)
            cost1=((n_cities-1)*(c_road))+c_lib
            
            #In case , placing library at each city is beneficial
            cost2=n_cities*c_lib
            
            #Considering each disconnected component and summing up the costs 
            total_cost+=min(cost1,cost2)
    return total_cost
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
