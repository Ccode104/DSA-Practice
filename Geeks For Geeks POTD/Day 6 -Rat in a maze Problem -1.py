from typing import List

class Solution:
    def findPath(self, matrix: List[List[int]]) -> List[str]:
        # code here
        
        result=[]
        def dfs(vertex:tuple,visited:list,path:list,matrix,n:int):
            
            if(vertex==(n-1,n-1)):
                #Reached the final destination
                string=str()
                for char in path:
                    string+=char
                result.append(string)
                
            else:
                #Try all possible ways
                
                for i in range(max(0,vertex[0]-1),min(n,vertex[0]+2)):
                    for j in range(max(0,vertex[1]-1),min(n,vertex[1]+2)):
                        if (i==vertex[0] or j==vertex[1])and(visited[i][j]!=1)and(matrix[i][j]!=0):
                            #Possible to move to (i,j)
                            visited[i][j]=1
                            if(vertex[0]!=i):
                                if(vertex[0]<i):
                                    path.append("D")
                                else:
                                    path.append("U")
                            else:
                                if(vertex[1]<j):
                                    path.append("R")
                                else:
                                    path.append("L")
                            dfs((i,j),visited,path,matrix,n)
                            visited[i][j]=0
                            path.pop()
            
        
        
        n=len(matrix)
        
        if(matrix[0][0]==0 or matrix[n-1][n-1]==0):
            pass
        else:
            visited=[[0 for i in range(n)]for j in range(n)]
            visited[0][0]=1
            
            path=[]
            
            dfs((0,0),visited,path,matrix,n)
            
            
        return result
            

#{ 
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))

# } Driver Code Ends