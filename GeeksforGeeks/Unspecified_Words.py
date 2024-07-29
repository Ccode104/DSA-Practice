#Reference:https://www.geeksforgeeks.org/googles-online-challenge-for-2021-intern-india-experience/?ref=ml_lbp

def match_count(dictionary:list,query:str,n:int,m:int):
    count=0 #Number of matches
    flag=0  #Indicates failure in matching when flag==1
    for word in dictionary:
        flag=0
        #Compare each word in dictionary with the query
        for i in range(m):
            #If a character does not match , check if the query has a '?'
            #at that place and accordingly conside it as matched
            if(word[i]!=query[i])and(query[i]!='?'):
                flag=1
                break
        #Succesful match, increment count
        if flag==0:
            count+=1
    return count

#Driver Code

import fileinput
 
filename = 'Unspecified_Words.txt'
 
data=fileinput.input(files=filename)

line=data.readline()
n,m=line.split()
n=int(n)
m=int(m)

dictionary=[]
for i in range(n):
    dictionary.append(data.readline())
Q=int(data.readline())
for i in range(Q):
    print(match_count(dictionary,data.readline(),n,m))




