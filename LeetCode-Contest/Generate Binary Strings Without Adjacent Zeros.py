#Reference:https://leetcode.com/contest/weekly-contest-405/
class Solution:                
    def validStrings(self, n: int) -> List[str]:
        
        def rec(n:int,sl:list,s:list):
            if(n==0):
                sl.append("".join(s))
            else:
                if(s.pop()=='1'):
                    s.append('1')
                    s.append('0')
                    rec(n-1,sl,s)
                    s.pop()
                    s.append('1')
                    rec(n-1,sl,s)
                    s.pop()
                    
                else:
                    s.append('0')
                    
                    s.append('1')
                    
                    rec(n-1,sl,s)
                    s.pop()
                              
        
        sl=[]
        s=['1']
        rec(n-1,sl,s)
        
        sl2=[]
        s=['0']
        rec(n-1,sl2,s)
        
        for i in sl2:
            sl.append(i)
        
        return sl