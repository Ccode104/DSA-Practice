class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        for operation in logs:
            if(operation=="../"):
                if(count>0):
                    count-=1
            elif(operation=="./"):
                pass
            elif(operation[len(operation)-1]=='/'):
                count+=1
        return count