#User function template for Python 3
#Reference:https://www.geeksforgeeks.org/problems/majority-element-1587115620/1

class Solution:
    def majorityElement(self, A, N):
        #Your code here

        #Calculate the frequency of each element in A and store it in a Hash Table

        freq=[0]*(max(A)+1)
        for i in A:
            freq[i]+=1
        match=N/2

        #Traverse the Hash Table to find the freq greater than N/2 
        for i in range(len(freq)):
            if freq[i]>match:
                return i
        
        #In case of no match
        return -1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends