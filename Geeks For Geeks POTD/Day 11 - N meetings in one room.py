#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here

       # Get a list of tuples - (start[i],end[i]) 
       meets=list(zip(start,end))
       
       # The criteria to sort based on 'end'
       def f(x):
          return x[1] 
       
       # Sort in ascending order of 'end'
       meets.sort(key=f)
                
       # Initially no meeting scheduled , so last=-1 and count=0
       # 'last' refers to 'end' of last meet scheduled
       last=-1
       count=0

       for i in range(n):
            # Check if the start of the meet[i] is greater than end of last meet 
            if(last<meets[i][0]):
                # meet[i] scheduled
                last=meets[i][1]
                count+=1
            else:
                pass
       return count
    
    # Note - We are sortng based on 'end' in ascending order 
    # because the meet that ends earliest will have least overlapping meets
    # If we sort based on start , then we may have the longest meet at first
    # thus reducing the number of meets

    # Pattern - smallest 'end' OR largest 'start'
                
                
               
    
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends