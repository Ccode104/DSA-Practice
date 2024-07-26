def Kth_smallest(arr:list,n:int,k:int):
    if(k==0):
        return -1
    
    res=arr[0]
    count=0
    freq=[0]*(max(arr)+1)
    for i in range(n):
        freq[arr[i]]+=1
    for i in range(0,max(arr)+1):
        count+=freq[i]
        if(count>=k):
            return i
    return -1

arr=[3,1,3,4,2,3,2,4,7,2,3,1]
print(Kth_smallest(arr,len(arr),3))
arr.sort()
print(arr)
