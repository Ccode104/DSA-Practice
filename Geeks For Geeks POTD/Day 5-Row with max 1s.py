#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr):
		# code here
		
		#Intialise to -1
		row_no=-1
		
		#No of elements in each row
		col_size=len(arr[0])
		
		#No of rows
		row_size=len(arr)
		
		#The minimum index(col_no) at which a '1' was found in a row
		min_index=col_size
		
		#Find a row corresponding to min_index
		for i in range(row_size):
		    for j in range(min_index):
		        if(arr[i][j]==1):
		            index=j
		            if(index<min_index):
		                row_no=i
		                min_index=index
		            break
		return row_no
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))

        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends