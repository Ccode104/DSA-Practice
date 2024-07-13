#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class PrimeTree {

public:
	void Sieve(int n, std::vector<int> &primes){
	  	std::vector<bool>prime(n+1, true);
	  	int p, i;
	  	for(p = 2; p*p <= n; p++){
		  	if(!prime[p])continue;
		  	for(i = p*p; i<=n ;i += p){
			  	prime[i] = false;
		  	}
	  	}
	  	for(i = 2; i <= n; i++){
		  	if(prime[i]){
			  	primes.push_back(i);
			}
		}
	  	return;
	}

  	bool isPrime(int n, std::vector<int>&prime){
	  	auto it = std::find(prime.begin(), prime.end(), n);
	  	return it != prime.end();
  	}

  	void dfs(int s, int p, int mod, std::vector<std::vector<int>> &adj, std::vector<std::vector<long long>>&dp, std::vector<int>&prime){
	  	int i, j;
	  	for(i=0; i<25; i++){
		  	dp[s][i] = 1;
	  	}
	  	for(auto u: adj[s]){
		  	if(u != p){
			  	dfs(u, s, mod, adj, dp, prime);
			  	for(i=0; i<25; i++){
				  	long long pos = 0;
				  	for(j=0; j<25; j++){
					  	if(!isPrime(prime[i] + prime[j], prime)){
						  	pos = (pos + dp[u][j])%mod;
					  	}
				  	}
				  	dp[s][i] = (dp[s][i] * pos) % mod;
			  	}
		  	}
	  	}
	  	return;
	}

  	int getNumberOfArrangements(int n, std::vector<std::vector<int>>&e){
	  	int i, j, mod = 1000000007;
	  	std::vector<int>primes;
	  	Sieve(200, primes);
	  	std::vector<std::vector<long long>>dp(n+1, std::vector<long long>(25, 0));
	  	std::vector<std::vector<int>>adj(n);
	  	for(i=0;i<n-1;i++){
		  	adj[e[i][0]].push_back(e[i][1]);
		  	adj[e[i][1]].push_back(e[i][0]);
	  	}
	  	dfs(0, -1, mod, adj, dp, primes);
	  	int ans = 0;
	  	for(i=0;i<25;i++){
		  	ans = (ans + dp[0][i]) % mod;
	  	}
	  	return ans;
	}

};

int main()
{
PrimeTree p;
vector<vector<int>> e={{0,1},{0,2}};
cout<<p.getNumberOfArrangements(3,e);
}