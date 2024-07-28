#User function Template for python3
class Solution:
	def removeDups(self, str):
		# code here
          
        #A hashtable to mark the presence of the character
        is_present=list()
        is_present=[0 for i in range(26)]

        n=len(str)
        
        #The output 
        result=""
        
        for i in range(n):
            if(is_present[ord(str[i])-ord('a')]==1):
                #It is present already
                pass
            else:
                #First occurence
                is_present[ord(str[i])-ord('a')]=1
                result=result+str[i]
        
        return result
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends