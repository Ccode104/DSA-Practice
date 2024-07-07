def subarray_sum(arr, n, sum):
    last = 0
    start = 0
    currsum = 0
    flag = False
    res = []

    # Iterate over the array
    for i in range(n):
        # Store sum up to current element
        currsum += arr[i]

        # Check if current sum is greater than or equal to given number
        if currsum >= sum:
            last = i

            # Start from starting index till current index(Reducing the size of subarray)
            while sum < currsum and start < last:
                # Subtract the element from left
                currsum -= arr[start]
                start += 1

            # If current sum becomes equal to given number
            if currsum == sum:
                res.append(start + 1)
                res.append(last + 1)
                flag = True
                break

    # If no subarray is found, store -1 in result
    if not flag:
        res.append(-1)

    # Return the result
    return res


# Driver Code
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum = 23
res = subarray_sum(arr, n, sum)
for i in res:
    print(i, end=" ")
