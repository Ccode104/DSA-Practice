def maximise(arr,n,m,s):
    print("s1 ",arr)
    if(m==0):
        return min(arr)
    i=j=0
    mini=min(arr)
    count=0
    while(arr.count(mini)==1)and(count<=m):
        inde=arr.index(mini)
        i=j=inde
        if(inde!=0):
            i=inde-1
        elif(inde!=n-1):
            j=inde+1
        print(i,j,s)
        while(j-i+1!=s):
            if(arr[i]<=arr[j])and(i!=0):
                i-=1
            elif(j!=n-1):
                j+=1
        print(i,j,s)
        for k in range(i,j+1):
            arr[k]+=1
        print("k1 ",arr)
        mini=min(arr)
        print(mini)
        print(arr.index(mini))
        count+=1
    j=-1
    print("s1 ",arr)
    if(count<m):
        i=arr.index(mini)
        for k in range(1,s):
            if arr[i+k]==mini:
                i=i
                j=i+s-1
        if(j!=-1):
            while(mini==min(arr))and(count<=m):
                for k in range(i,j+1):
                    arr[k]+=1
                print("s2 ",arr)
            if(count==m):
                return mini
            else:    
                maximise(arr,n,m-count,s)
        else:
            while(arr.count(mini)!=1)and(count<=m):
                inde=arr.index(mini)
                if(inde!=0):
                    i=inde-1
                elif(inde!=n-1):
                    j=inde+1
                while(j-i+1!=s):
                    if(arr[i]<arr[j])and(i!=0):
                        i-=1
                    elif(j!=n-1):
                        j+=1
                for k in range(i,j+1):
                    arr[k]+=1
                print("s3 ",arr)
                mini=min(arr)
                count+=1
            maximise(arr,n,m-count,s)
    else:  
        return min(arr) 
    return min(arr)           
arr=[1,2,3,4,5,6]
print(maximise(arr,6,5,2))              
