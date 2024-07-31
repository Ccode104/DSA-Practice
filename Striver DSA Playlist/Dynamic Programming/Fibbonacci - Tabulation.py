
n=5
dp=[0 for i in range(n+1)]

#Initialise acc to base case
dp[0]=0
dp[1]=1

#Now look for the recursie statement
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[n])

# We observe that we need previous 2 elements only

prev2=0
prev1=1

for i in range(2,n+1):
    curr=prev1+prev2
    prev2=prev1
    prev1=curr
print(curr)