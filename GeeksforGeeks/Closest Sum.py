import sys

class Solution:
    def closest3Sum(self, A, N, X):
        # code here

        #Sort the array
        A.sort()

        sum=0
        closestSum=1000000

        #Fix the first element of the triplet as A[i] and move j and k to inc or dec sum
        for i in range(N-2):
            j=i+1
            k=N-1

            while(j<k)and(closestSum!=X):
                sum=A[i]+A[j]+A[k]


                if(abs(sum-X)<abs(closestSum-X)):
                    closestSum=sum
                elif(abs(sum-X)==abs(closestSum-X)):
                    closestSum=max(sum,closestSum)
                    
                if(sum<X):
                    j+=1
                else:
                    k-=1
            if(closestSum==X):
                break
        return closestSum
                
                
            
        
        


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
        X = int(input())
        ob = Solution()
        print(ob.closest3Sum(Arr, N, X))
# } Driver Code Ends