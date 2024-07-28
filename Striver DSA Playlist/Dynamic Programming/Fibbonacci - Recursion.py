
def fibbonacci(n:int):

    #First Term
    if(n==1):
        result=0
    #Second Term
    elif(n==2):
        result=1
    #nth term(n>2)
    else:
        result=fibbonacci(n-1)+fibbonacci(n-2)
    
    return result

# 0 1 1 2 ...
print(fibbonacci(4))
# Output : 2