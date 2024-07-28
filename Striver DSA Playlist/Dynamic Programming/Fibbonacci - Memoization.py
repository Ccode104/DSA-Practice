import sys

# After observing the Recursion tree , we come across overlapping subproblems
# We do memoization, i.e we create an array to store the outputs of each subproblem

def fibbonacci(n:int,dp:list)->int:

    # Already Solved
    if(dp[n]!=-1):
        result=dp[n]
    # First Term
    if(n==1):
        result=0
    # Second Term
    elif(n==2):
        result=1
    # nth term(n>2)
    else:
        result=fibbonacci(n-1,dp)+fibbonacci(n-2,dp)
    
    # Store the result
    dp[n]=result
    return result

# Array to store the output of each subproblem
# Assuming the constraint : 1=<n<100
dp=[-1 for i in range(100)]

print(fibbonacci(4,dp))