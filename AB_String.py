def count(m,n,sum,no):
    if(sum<0):
        return False
    if(n==0):
        no+=1
    if(sum==0):
        #Append 'A
        count(m,n-1,sum-1,no)
    else:
        #Append 'A' or 'B
        count(m,n-1,sum-1,no)
        count(m-1,n,sum+1,no)
no=0
m=2
n=2
count(m-1,n,1,no)
print(no)