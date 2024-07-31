def min_cost(seq)->int:
    if(len(seq)==0):
        result=0
    else:
        bal=1
        n=len(seq)
        index=0
        for i in range(1,n):
            if(seq[i]=='('):
                bal+=1
                index=i
            elif(seq[i]==')'):
                bal-=1
                
            else:
                if(bal>=0):
                    bal+=1
                    cost+=i-index
                else:

        
