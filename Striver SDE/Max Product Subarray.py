class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        j=0
        n=len(nums)
        
        #Stores the product of subarray starting from left
        prefix_prod=1

        #Stored the product of subarray starting from right
        suffix_prod=1

        max_prod=-11

        while(j<n):
            
            # If we had encountered a zero in any of the subarrays
            # We mark the beginning of a new subarray
            if(prefix_prod==0):
                prefix_prod=1
            if(suffix_prod==0):
                suffix_prod=1

            prefix_prod*=nums[j]
            suffix_prod*=nums[n-1-j]
            
            max_prod=max(max_prod,max(suffix_prod,prefix_prod))
            
            j+=1
        return max_prod

'''
A Zero must be excluded so we make a new subarray
A negative number's both side subarray's max must be chosen
'''