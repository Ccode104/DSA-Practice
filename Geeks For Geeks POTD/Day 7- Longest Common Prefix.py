#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        
        #Sort the strings
        arr.sort()
        
        i=0
        
        #Number of Strings
        n=len(arr)
        
        #Length of smallest/first string
        m=len(arr[0])

        result=""
        
        while(i<m):
            flag=0
            # Compare the ith character of first string with rest of strings
            for j in range(1,n):
                if(arr[j][i]==arr[0][i]):
                    pass
                else:
                    flag=1
                    break
            # If all have it as prefix
            if(flag==0):
                result+=arr[0][i]
            else:
                break
            i+=1
        
        # If no common prefix
        if(len(result)==0):
            result="-1"
        
        return result
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends