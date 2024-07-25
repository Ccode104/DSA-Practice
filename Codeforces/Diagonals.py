
def minimum_possible_diagonals(n:int,k:int):
    
    count=0
    if(n>=k):
        if(k!=0):
            count+=1
        return count
    k=k-n
    count+=1
    i=n-1
    while(i>=1):
        if(i>=k):
            count+=1
            break
        else:
            k=k-i
            count+=1
        if(i>=k):
            count+=1
            break
        else:
            count+=1
            k=k-i
        i-=1
    return count

t=int(input())
    
for i in range(t):
    l=input()
    l=list(l.split())
    n=int(l[0])
    k=int(l[1])
    print(minimum_possible_diagonals(n,k))