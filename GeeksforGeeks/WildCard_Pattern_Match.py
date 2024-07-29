def isMatch(string,pattern,n,m):
    i=0
    j=0 
    lastWild=-1
    lastMatchWithWild=0
    while i<n:
        if j<m and (pattern[j]==string[i]or pattern[j]=='?'):
            i+=1
            j+=1
        elif j<m and pattern[j]=='*':
            lastWild=j
            lastMatchWithWild=i
            j+=1
        elif lastWild!=-1:
            j=lastWild+1
            lastMatchWithWild=lastMatchWithWild+1
            i=lastMatchWithWild
        else:
            return False
    while j<m and pattern[j]=='*':
        j+=1
    return j==m

# Driver code


strr = "baaabab"
pattern = "*****ba*****ab"

if (isMatch(strr, pattern, len(strr),len(pattern))):
    print("Yes")
else:
    print("No")

            