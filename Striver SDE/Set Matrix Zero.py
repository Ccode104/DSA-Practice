
def set_matrix_zero(mat:list[list],x:int,y:int):
    zeroes=list()

    for i in range(x):
        for j in range(y):
            if(mat[i][j]==0):
                zeroes.append((i,j))
    for (row,col) in zeroes:
        for i in range(x):
            mat[i][col]=0
        for j in range(y):
            mat[row][j]=0
    return mat

mat=[[1,1,1],[1,0,1],[1,1,1]]
print(set_matrix_zero(mat,len(mat),len(mat[0])))

     