
def max_cost(password:str)->str:
    result=str()
    if(len(password)==0):
        result=str(password+'a')

    else:

        n=len(password)
        
        cost=[0 for i in range(n)]
        cost[0]=2
        
        index=-1
        for i in range(1,n):
            if(password[i]!=password[i-1]):
                cost[i]=2
            else:
                if(cost[i-1]==2):
                    index=i
                cost[i]=1
    
        if(index!=-1):
            #If '1' exists
            if(index!=n-1):
                for i in range(ord('z')-ord('a')+1):
                    if(ord(password[index+1])-ord('a')!=i)and(ord(password[index-1])-ord('a')!=i):
                        break
                
                result=password[0:index]+chr(i+ord('a'))+password[index:n]
            else:
                for i in range(ord('z')-ord('a')+1):
                    if(ord(password[index-1])-ord('a')!=i):
                        break
                result=password[0:index]+chr(i+ord('a'))+password[index:n]
        else:
            for i in range(ord('z')-ord('a')+1):
                    if(ord(password[0])-ord('a')!=i):
                        break
            result=chr(i+ord('a'))+password
   
    return result

            
t=int(input())
for i in range(t):
    password=input()
    print(max_cost(password))


