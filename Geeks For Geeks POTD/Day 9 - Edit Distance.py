class Solution:
	def editDistance(self, str1, str2):
		# Code here
		
		length1,length2=len(str1),len(str2)
		
		# dp[i][j] denotes the number of operations required 
		# to convert str[0:i+1] to str2(0:j+1)
          
        dp=[[0 for j in range(length2+1)] for i in range(length1+1)]
        
        # Tabulation Method
        for i in range(length1+1):
            for j in range(length2+1):
                # Base case
                if i==0 or j==0:
                    # if a string str1 of length 0 is to be converted to 
                    # another string str2, we need len(str2) insertions
                    
                    # if a string str2 of length 0 is to be obtained from 
                    # another string str1, we need len(str2) deletions
                    
                    # if both are emty , we need '0' operations
                    
                    dp[i][j]=i|j
                else:
                    # Recursive Case
                    if str1[i-1]==str2[j-1]:
                        # If str1[i-1] == str2[j-1] ,
                        # then: we need no extra operations 
                        # to get the string str2[0:j+1] from
                        # str1[0:i+1]
                        dp[i][j]=dp[i-1][j-1]
                        
                    else:
                         # In case not equal, we have 3 choices:
                         # replace,insert or delete
                         # insert/delete : dp[i][j-1] , dp[i-1][j]
                         # replace : dp[i-1][j-1]
                        dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
        return dp[length1][length2]
                    
                
                
                


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.editDistance(s, t)
        print(ans)

# } Driver Code Ends