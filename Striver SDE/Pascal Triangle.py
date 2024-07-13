class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1],[1,1]]
        prev_row=[1,1]
        curr_row=[1,1]
        for i in range(1,numRows-1):
            for j in range(i):
                curr_row.insert(j+1,prev_row[j]+prev_row[j+1])
            res.append(curr_row)
            prev_row=curr_row
            curr_row=[1,1]
        if(numRows==1):
            return [[1]]
        else:
            return res