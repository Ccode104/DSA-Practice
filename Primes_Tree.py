def getNumberOfArrangements(N: int, edges: list[list[int]]) -> int:	
						
	#Adjacency matrix
	adj=[[0 for i in range(N)]for j in range(N)]
		
    #Fill the matrix
	#adj[i][j] means [i,j] is a edge
	for e in edges:
	    adj[e[0]][e[1]]=1
    
    
	prime=[ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	count=0
	
    if(N!=1):
		for p in prime:
			vals=[0 for i in range(N)]
			
           #Let the root be assigned p
			vals[edges[0][0]]=p
				
			c=0
				
			count+=rec(edges[0][0],inv,adj,c,vals,prime)
		return count%1000000007
	else:
	    return 25%1000000007

N=3
edges=[[0,1],[0,2]]
print(getNumberOfArrangements(N,edges))