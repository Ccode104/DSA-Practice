def isinterleaved(A,B,C):
    M=len(B)
    N=len(C)

    dp=[[False for i in range(N)]for j in range(M)]

    if(M+N!=len(A)):
        return False
    
    for i in range(0,M):
        for j in range(0,N):

            if(i==0)and(j==0):
                #Both subs of B and C considered of len 0
                dp[0][0]=True
            elif(i==0)and(C[j-1]==A[i+j-1]):
                dp[i][j]=dp[i][j-1]
            elif(j==0)and(B[i-1][j]==A[i+j-1]):
                dp[i][j]=dp[i-1][j]
            else:
                if(A[i+j-1]==B[i-1])and(A[i+j-1]!=C[j-1]):
                    dp[i][j]=dp[i-1][j]
                elif(A[i+j-1]!=B[i-1])and(A[i+j-1]==C[j-1]):
                    dp[i][j]=dp[i][j-1]
                else:
                    return False
    return dp[M-1][N-1]
                
# A function to run test cases 
def test(A, B, C): 

    if (isinterleaved(A, B, C)): 
        print(A, "is interleaved of", B, "and", C) 
    else:
        print(A, "is not interleaved of", B, "and", C)

# Driver Code 
if __name__ == '__main__': 
    test("XXZXXXY","XXY", "XXZ") 
    test("WZXY","XY", "WZ") 
    test("XXY","XY", "X") 
    test("XXY","YX", "X") 
    test("XXXXZY","XXY", "XXZ") 
    
