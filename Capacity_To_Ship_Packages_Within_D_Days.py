
def isValid(weights,D,n,mx):

    num_of_days=1
    sum=0

    for i in range(0,n):
        sum+=weights[i]

        if(sum>mx):
            num_of_days+=1
            sum=weights[i]
        if(num_of_days>D):
            return False
    return True

def shipWithinDays(weights,D,n):

    r=sum(weights)
    l=max(weights)
    res=r
    while(l<=r):
        mid=l+(r-l)//2

        if(isValid(weights,D,n,mid)):
            res=min(mid,res)
            r=mid-1
        else:
            l=mid+1
    return res

# Driver Code
if __name__ == '__main__':
     
    weight = [ 9, 8, 10 ]
    D = 3
    N = len(weight)
     
    print(shipWithinDays(weight, D, N))