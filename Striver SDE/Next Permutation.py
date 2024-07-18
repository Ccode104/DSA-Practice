class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #If the number is of length 1 then only single permutation is possible
        if(len(nums)==1):
            pass
        else:
            #Find the smallest number greater than the element at index 'i' in nums[i+:]
            i=len(nums)-2
            while(i>=0):
                res=101
                for j in range(i+1,len(nums)):
                    if(nums[j]>nums[i]):
                        if(nums[j]<res):
                            res=nums[j]
                            index=j
                #if no such element exists ,decrement i and repeat
                if(res==101):
                    i-=1
                else:
                #Once found , do a swap and sort remaining (nums[i+1:])    
                    j=index
                    temp=nums[j]
                    nums[j]=nums[i]
                    nums[i]=temp
                    nums[i+1:]=sorted(nums[i+1:])
                    break
            if(i==-1):
                #It is the last permutation, so return the first one
                nums.sort()
        return nums
        