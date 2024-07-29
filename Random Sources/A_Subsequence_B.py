def min_elements_to_add(A, B, n, m):
    # Find the common elements in both A and B
    common_elements = set(A).intersection(set(B))
    
    # Initialize an array to store the index of elements in A
    index_array = [1000000] * (max(common_elements) + 1)
    for elem in common_elements:
        index_array[elem] = A.index(elem)
    index_array.sort()
    
    # Length of common elements
    length_common = len(common_elements)
    
    # Create a list of common elements in the order they appear in A
    ordered_common_elements = [A[index_array[i]] for i in range(length_common)]

    # Frequency of common elements in B
    frequency = [-1] * (max(common_elements) + 1)
    for elem in ordered_common_elements:
        frequency[elem] = B.count(elem)

    # Initialize variables
    flag = 0
    count = 0
    max_count = 0
    i = 0

    # Traverse through the common elements to count matches
    while i < length_common and flag == 0:
        count = 0
        for j in range(m):
            if B[j] == ordered_common_elements[i] and i < length_common:
                frequency[ordered_common_elements[i]] -= 1
                i += 1
                count += 1
            if i == length_common:
                break
            for freq in frequency:
                if freq != 0:
                    break
                else:
                    flag = 1
        
        if max_count < count:
            max_count = count

    # The number of elements that need to be added to B
    return n - max_count

# Driver code
A = [1, 2, 3, 4, 5]
B = [2, 5, 6, 4, 9, 12]

print(min_elements_to_add(A, B, len(A), len(B)))  # Output: 3


'''
Rough Code:

def subsequence(A,B,n,m):
    #Common
    C=set(A).intersection(set(B))
    #Missing in B
    D=set(A).difference(C)
    
    indexi=[1000000]*(max(C)+1)
    for i in C:
        indexi[i]=A.index(i)
    indexi.sort()
    l=len(C)
    C=[A[indexi[i]] for i in range(l)]

    freq=[-1]*(max(C)+1)
    for i in C:
        freq[i]=B.count(i)

    flag=0
    count=0
    maxi=0
    i=0

   
    while(i<l)and flag==0:
        count=0
        for j in range(m):
            if(B[j]==C[i])and(i<l):
                freq[C[i]]-=1
                i+=1
                count+=1
            if i==l:
                break
            for k in freq:
                if k!=0:
                    break
                else:
                    flag=1
        
        if(maxi<count):
            maxi=count
    return n-maxi
#Driver

A=[1,2,3,5]
B=[1,2,5,6,4,9,12]   

print(subsequence(A,B,len(A),len(B)))

    
'''