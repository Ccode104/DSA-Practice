#User function Template for python3

from collections import defaultdict
class Solution:
    def findSubArraySum(self, arr, n, k):
        # code here

        #It stores the number of subarrays with sum=sums key-value
        #value=freq
        #key=sum

        freq=defaultdict(lambda:0)

        count=0    
        sum=0

        #We consider only the subarray starting from index 0
        for i in range(n):
            sum+=arr[i]

            #If sum!=k then we find the diff in the freq hash table
            #i.e we remove that diff subarray from the main subarray to get reqd sum

            if(sum==k):
                count+=1
            #Note:We do not have a elif here to accomodate the case of k=0
            if(freq[sum-k]!=0):
                count+=freq[sum-k]
            
            freq[sum]+=1
        return count


     


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.findSubArraySum(Arr, N, k))
# } Driver Code Ends