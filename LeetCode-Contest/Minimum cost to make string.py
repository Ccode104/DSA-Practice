### Trie-tree implementation
class TrieNode:
    def __init__(self):
        #Dictionary to store child trie nodes
        self.children = {}

        #Impossible cost(Termination)
        self.cost = 10**10

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, cost):
        #Point to the root
        node = self.root

        #Search for the characters in word in trie(No duplication!)
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.cost = min(cost, node.cost)
    
    def search(self, s, start):
        #Start the search from root
        node = self.root
        matches = []

        #Search for char in s[start:] in trie 
        for i in range(start, len(s)):
            if s[i] in node.children:
                #Found it!
                node = node.children[s[i]]

                #Check the cost to verify
                if node.cost < 10**10:
                    matches.append((i + 1, node.cost))
            else:
                break
        return matches

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        n, m = len(target), len(words)
    
        trie = Trie()
        for word, cost in zip(words, costs):
            trie.insert(word, cost)
    
        dp = [10 ** 10] * (n + 1)
        dp[0] = 0 
    
        for i in range(n):
            if dp[i] >= 10**10:
                continue
            
            matches = trie.search(target, i)
            for idx, cost in matches:
                dp[idx] = min(dp[idx], dp[i] + cost)
        
        result = dp[n]
        return result if result < 10**10 else -1
