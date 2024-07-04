#This function counts the number of strings possible 
#from 'm' Bs and 'n' As such that the corresponding 
# prefix array will have only +ve nos
def count(m,n,sum,no):
    if m+sum<n:
        return no
    if(sum<0):
        #Further extension of string not possible
        return no
    if(n==0):
        #If the number of As have exhausted then the string must be valid
        no+=1
        return no
    if(sum==0):
        #Append 'B' since sum cannot get -ve
        no=count(m-1,n,sum+1,no)
    else:
        #Append 'A' or 'B
        no=count(m,n-1,sum-1,no)
        if(m!=0):
            no=count(m-1,n,sum+1,no)
    return no

m=3 #Number of As
n=3 #Number of Bs

print("Number of possible combinations is ",count(m-1,n,1,0))