def op(arr:list,q:int,x:int):
    if(q==1):
        arr.append(x)
    else:
        for i in range(len(arr)):
            arr[i]^=x
    arr.sort()
    print(arr)

import fileinput

filename='XOR_op.txt'
data=fileinput.input(files=filename)

n=int(data.readline())

arr=[0]

for i in range(n):
    line=data.readline()
    q,x=line.split()
    q=int(q)
    x=int(x)
    op(arr,q,x)

