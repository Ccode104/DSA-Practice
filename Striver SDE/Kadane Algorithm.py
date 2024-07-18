class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        i=0
        j=0
        n=len(nums)
        sum=0
        maxsum=-sys.maxsize
        while(i<n)and(j<n):
            sum=sum+nums[j]
            if(maxsum<sum):
                maxsum=sum
            if(sum<0):
                sum=0
                i=j
            j+=1
        return maxsum
        