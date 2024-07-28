#Using Memoization i.e saving the output of each function call possible in an array dp

def lcs(x,y,m,n,dp):

    #If there are no more characters in x or y remaining to be considered
    if(m==0 or n==0):
        dp[0][0]=0
        return dp[0][0]
    
    #Do not solve the same subproblem again
    elif(dp[m][n]!=-1):
       return dp[m][n]
    
    #Starting from the last character of each string
    elif(x[m-1]==y[n-1]):
        dp[m][n]=1+lcs(x,y,m-1,n-1,dp)
        return dp[m][n]
    else:
       t1=lcs(x,y,m-1,n,dp)
       t2=lcs(x,y,m,n-1,dp)
       if(t1>t2):
        dp[m][n]=t1
       else:
        dp[m][n]=t2
       return dp[m][n]
# Driver code


X = "AGGTAB"
Y = "GXTXAYB"

m = len(X)
n = len(Y)
dp = [[-1 for i in range(n + 1)]for j in range(m + 1)]

print(f"Length of LCS is {lcs(X, Y, m, n, dp)}")