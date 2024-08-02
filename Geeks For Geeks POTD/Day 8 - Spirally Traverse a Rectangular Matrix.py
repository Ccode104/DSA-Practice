class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    # Approach : Solve the problem for a Square Matrix first  
    def spirallyTraverse(self, matrix):
        # code here
        
        rows=len(matrix)
        cols=len(matrix[0])
        
        def traverse(start_col:int,end_col:int,start_row:int,end_row:int,matrix,result):
            
            # If the matrix has only 1 row 
            if(start_row==end_row):
                i=start_row
                for j in range(start_col,end_col+1):
                    result.append(matrix[i][j])
            
            # If the matrix has only 1 column
            elif(start_col==end_col):
                j=start_col
                for i in range(start_row,end_row+1):
                    result.append(matrix[i][j])
            
            # If matrix is empty
            elif(start_row>end_row)or(start_col>end_col):
                pass
            
            # If neithr of above cases
            else:
                
                # Upper Boundary
                i=start_row
                for j in range(start_col,end_col+1):
                    result.append(matrix[i][j])
                 
                # Right Boundary
                j=end_col
                for i in range(start_row+1,end_row+1):
                    result.append(matrix[i][j])
                    
                # Bottom Boundary
                i=end_row
                for j in range(end_col-1,start_col-1,-1):
                    result.append(matrix[i][j])
                
                # Left Boundary
                j=start_col
                for i in range(end_row-1,start_row,-1):
                    result.append(matrix[i][j])
                
                # Note : We have left the corne elements so they don't repeat
                
                # Traverse the inner matrix
                traverse(start_col+1,end_col-1,start_row+1,end_row-1,matrix,result)
                
            return result
        
        
        # Call the recursive function traverse
        
        result=list()
        
        result=traverse(0,cols-1,0,rows-1,matrix,result)
        
        return result
                
                


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))

# } Driver Code Ends