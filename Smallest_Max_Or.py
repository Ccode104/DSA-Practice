def smallestSubset(arr,n):
    start=0
    end=0
    freq=[0 for i in range(max(arr)+1)]
    s=set(arr)
    l=[]
    l.extend(s)
    l.sort()
    for j in range(len(l)):
        res=res|l[j]
    for i in range(len(l)):
        res=res|l[len(l)-1-i]
        if(max<res):
            max=res
            length=len
        


    



arr=[2, 6, 2, 8, 4, 5]
smallestSubset(arr,len(arr))
print(8|6|5|4)


''' while end<n and start<=end:
        freq[arr[end]]+=1
        if(freq[arr[start]]>1):
            start+=1
        end+=1
    print(arr[start:end+1])'''