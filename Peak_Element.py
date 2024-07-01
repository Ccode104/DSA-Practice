

def peakElement(arr, n) :
    if (n == 1) : 
        return 0
    else:
        for i in range(1,n-1):
            if(arr[i-1]<=arr[i])and(arr[i]>=arr[i+1]):
                return i
    if (arr[n - 1] >= arr[n - 2]):
        return n-1

