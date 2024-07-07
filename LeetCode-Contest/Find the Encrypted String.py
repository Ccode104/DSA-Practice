#Reference:https://leetcode.com/problems/find-the-encrypted-string/

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        
        l=len(s)
        arr=list(s)
        for i in range(0,l):
            arr[i]=s[(i+k)%l]
        return "".join(arr)