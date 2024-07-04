#This functions checks if a subset exists in the set[0...n-1] with the sum = sum
def isSubsetSum_rec(set,n,sum):
    if(n==0):
        return False
    if(sum==0):
        return True
    if(set[n-1]>sum):
        #We ignore the element ser[n-1]
        return isSubsetSum_rec(set,n-1,sum)
    
    #We consider the two cases:
    #    1-Include set[n-1]
    #    2-Exclude it
    return isSubsetSum_rec(set,n-1,sum) or isSubsetSum_rec(set,n-1,sum-set[n-1])

#Implementing the same using Memoization



def isSubsetSum_mem(set,n,sum):
    if(n==0):
        return False
    if(sum==0):
        return True
    if(table[n][sum]!=-1):
        return table[n][sum]
    if(set[n-1]>sum):
        table[n-1][sum]=isSubsetSum_mem(set,n-1,sum)
        return table[n-1][sum]
    table[n-1][sum]=isSubsetSum_mem(set,n-1,sum)
    table[n-1][sum-set[n-1]]=isSubsetSum_mem(set,n-1,sum-set[n-1])

    return table[n-1][sum] or table[n-1][sum-set[n-1]]

#Using DP

def isSubsetSum_dp(set,n,sum):
    table=[[False for i in range(sum+1)]for j in range(n+1)]

    for i in range(n+1):
        table[i][0]=True
        table[0][i]=False

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if(set[i-1]>j):
                table[i][j]=table[i-1][j]
            else:
                table[i][j]=table[i-1][j] or table[i-1][j-set[i-1]]
    return table[n][sum]

#Space optimisation

def isSubsetSum(set,n,sum):

    prev=[False for i in range(sum+1)]
    curr=[False for i in range(sum+1)]

    for i in range(1,n+1):
        prev[0]=True
        for j in range(1,sum+1):
            if(set[i-1]>j):
                curr[j]=prev[j]
            else:
                curr[j]=prev[j] or prev[j-set[i-1]]
        prev=curr
    return prev[sum]
# Driver Code
if __name__ == '__main__':
    n = 5
    a = [1, 5, 3, 7, 4]
    sum = 12
    table=[[-1 for i in range(sum+1)]for j in range(n+1)]
    if (isSubsetSum(a, n, sum)):
        print("YES")
    else:
        print("NO")

