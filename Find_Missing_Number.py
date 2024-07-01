def missing_no(arr,n):
    sum=0
    for i in arr:
        sum+=i
    return ((n*(n+1))/2)-sum

arr=[1,2,3,5,6]

print(missing_no(arr,6))