class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n=len(prices)

        #It contains the max element in each contiguos subarray ending at prices[-1]
        max_sp_array=[0,prices[-1]]
        
        max_profit=0
        
        max_sp=prices[-1]
        
        #Compute and fill max_sp_array
        for i in range(2,n):
            if(max_sp<prices[-i]):
                max_sp=prices[-i]
            max_sp_array.append(max_sp)

        #Compute max_profit
        for i in range(n-1):
            purchase_price=prices[i]

            #Find max of rem array
            max_sp=max_sp_array[n-1-i]

            if(max_profit<max_sp-purchase_price):
                max_profit=max_sp-purchase_price
        return max_profit
    
    #Time Complexity:O(n)
    #Space Complexity:O(n)
    