#Using the same array as a hashtable for numbers in range 1 to N

def smallest_miss_pos_no(arr,n):
    for i in range(0,n): 
        while 0<arr[i]<=n and arr[i]!=arr[arr[i]-1]:
            t=arr[i]
            arr[i]=arr[arr[i]-1]
            arr[t-1]=t
    for i in range(0,n):
        if(arr[i]!=i+1):
            return i+1
    return n+1

# Driver code
if __name__ == '__main__':
    arr = [0, 10, 2, -10, -20]
    n = len(arr)
    ans = smallest_miss_pos_no(arr, n)
    print(ans)

#Reference:https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/