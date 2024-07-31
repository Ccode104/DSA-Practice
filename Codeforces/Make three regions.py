def block(matrix,)->int:

    n=len(matrix[0])
    result=0
    count=0
    for i in range(2):
        for j in range(n):
            if(matrix[i][j]=='x'):
                count+=1
    
    
    
    if(count==0):
        #Completly connected region
        result=0
    else:
        i=0
        for j in range(1,n-1):
            if(matrix[i][j]=='.'):
                #Check for adjacent blocked blocks
                if(matrix[i+1][j]!='x')and(matrix[i+1][j-1]=='x')and(matrix[i+1][j+1]=='x')and(matrix[i][j-1]!='x')and(matrix[i][j+1]!='x'):
                    result+=1
        i=1
        for j in range(1,n-1):
            if(matrix[i][j]=='.'):
                #Check for adjacent blocked blocks
                if (matrix[i-1][j]!='x')and(matrix[i-1][j-1]=='x')and(matrix[i-1][j+1]=='x')and(matrix[i][j-1]!='x')and(matrix[i][j+1]!='x'):
                   result+=1
        
    return result

t=int(input())

for test in range(t):
    n=int(input())
    matrix=[]
    for i in range(2):
        matrix.append(list(input()))
    
    print(block(matrix))
'''
4
8
.......x
.x.xx...
2
..
..
3
xxx
xxx
9
..x.x.x.x
x.......x'''
