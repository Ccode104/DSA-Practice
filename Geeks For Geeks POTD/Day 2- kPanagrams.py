#User function Template for python3
class Solution:
    def kPangram(self,string, k):
    # code here
    
        #Get all the substrings - ignoring spaces
        list_of_substrings=string.split()
    
        #print(list_of_substrings)
        
        #Mark the characters present in the string
        alphabets=[0 for i in range(26)]
        for sub in list_of_substrings:
            for character in sub:
                alphabets[ord(character)-ord('a')]=1
        
        
        #Count the number of characters missing
        
        missing=alphabets.count(0)
        
        #Check if 'k' operations are sufficient
        if(k>=missing):
            result=True
        else:
            result=False
        
        #Check if the string has atleast 26 characters
        total_len=[len(sub) for sub in list_of_substrings]
        total_len=sum(total_len)
        
        if(total_len<26):
            result=False
        
        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends