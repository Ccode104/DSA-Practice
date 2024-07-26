def smallestSubset(arr,n):
    maxOr=0
    for i in range(n):
        maxOr=maxOr|arr[i]
    
    
    count=[float('inf') for i in range(maxOr+1)]

    count[0]=0
    #print(maxOr)
    for i in range(n):
        temp=[float('inf') for i in range(maxOr+1)]
        for j in range(maxOr+1):
            temp[j]=min(temp[j],count[j])
            if(count[j]!=float('inf')):
                #print(j|arr[i])
                temp[j|arr[i]]=min(temp[j|arr[i]],count[j]+1)
        count=temp
    return temp[maxOr]

if __name__ == '__main__':
    data = [5, 1, 3, 4, 2] 
    sz = len(data)

    # Function Call
    print(smallestSubset(data, sz))
        


    






''' while end<n and start<=end:
        freq[arr[end]]+=1
        if(freq[arr[start]]>1):
            start+=1
        end+=1
    print(arr[start:end+1])'''