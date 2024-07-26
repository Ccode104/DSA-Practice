#Reference:
#https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        index=-1
        for i in range(1,len(number)-1):
            if(number[i]==digit[1]):
                if(i==1):
                    if(number[i]<=number[i-1]):
                        index=i
                        break
                    else:
                        index=i
                else:
                    if(number[i]>=number[i-1]):
                        index=i
                        break
                    else:
                        index=i
        new=list(number)
        if(index!=-1):
            new.pop(i)
        print("".join(new))

string=input()
digit=input()

Solution.removeDigit(Solution,string,digit)