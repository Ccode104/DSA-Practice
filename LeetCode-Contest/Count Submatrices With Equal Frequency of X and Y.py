#It is a problem that has the usecase of prefix sum
#Reference:https://leetcode.com/contest/weekly-contest-405/

class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        m=len(grid[0]) #Cols
        n=len(grid) #Rows
        res=0

        #Denotes the presence of 'X'
        cnt1=[[1 if grid[i][j]== 'X' else 0 for j in range(m) ]for i in range(n)]

        #Same applies for 'Y
        cnt2=[[1 if grid[i][j]== 'Y' else 0 for j in range(m) ]for i in range(n)]

        #Maintains the prefix sum or denotes the number of 'X' in a grid 
        # with the corner (i,j) opp to (0,0)
        for i in range(1,n):
            for j in range(m):
                cnt1[i][j]+=cnt1[i-1][j]
                cnt2[i][j]+=cnt2[i-1][j]
        

        for i in range(n):
            for j in range(1,m):
                cnt1[i][j]+=cnt1[i][j-1]
                cnt2[i][j]+=cnt2[i][j-1]
        
        for i in range(n):
            for j in range(m):
                if cnt1[i][j]>0 and cnt1[i][j]==cnt2[i][j]:
                    #Freq of X and Y equal
                    #Atleast one X
                    res+=1
                    
        return res

grid=[["X","Y","."],["Y",".","."]]

print("Number of Submatrices possible = ",Solution.numberOfSubmatrices(Solution,grid))