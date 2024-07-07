from sys import maxsize

def kadane(arr:list,n:int):

    max_so_far=0
    max_till_here=-maxsize-1
    i=0
    st=0
    en=0

    while(i<n):
        max_till_here+=arr[i]

        if(max_till_here>max_so_far):
            en=i
            max_so_far=max_till_here
        if(max_till_here<0):
            st=i+1
            en=i+1
            max_till_here=0
        i+=1

        if(en-st>=1)and(en<n):
            return max_so_far
        else:
            return max(arr)

# Driver program to test maxSubArraySum
a = [-1,-2,-3,-4]
print(kadane(a, len(a)))

