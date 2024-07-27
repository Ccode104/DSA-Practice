#User function Template for python3

class Solution:
    def countMin(self, str):
        # code here
        def lcs(x,y,m,n,dp):

            if(m==0 or n==0):
                dp[0][0]=0
                return dp[0][0]
            elif(dp[m][n]!=-1):
                return dp[m][n]
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
        
        
        n=len(str)
        i=0
        while (i<n) and (str[i]==str[n-1-i]) :
            i+=1
        
        if(i==n):
            # Palindrome
            result = 0
        else:
            # Not a palindrome
            
            # Ignore the matching outer layer
            str=list(str[i:n-i])

            # Reverse it
            rev_str=list(str)
            rev_str.reverse()
            
            m=n=len(str)
            dp = [[-1 for i in range(n + 1)]for j in range(m + 1)]
            
            # Find the length of the Longest Palindromic Subsequence
            # We observe that this is LCS of str and its reverse(rev_str)
            # Therefore , we only need to take care of the the elements not in the LCS
            # Hence, we need an insertion each for such elements 
            
            result=len(str)-lcs(str,rev_str,m,n,dp)    
            
        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.countMin(Str))

# } Driver Code Ends