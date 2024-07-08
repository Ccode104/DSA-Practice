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
        # We update the cost of only the last node(char)
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

                #Check the cost to verify if it is the end in the trie 
                if node.cost < 10**10:
                    matches.append((i + 1, node.cost))
            else:
                break
        # We are actually searching for all the prefixes
        # (but the longest ones from each word)
        #  of s[start:] and storing their len and cost in matches=[] 
        # eg : abcd has a,ab,abc,abcd as prefixes
        return matches

class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        n, m = len(target), len(words)
    
        trie = Trie()
        for word, cost in zip(words, costs):
            trie.insert(word, cost)
    
        dp = [10 ** 10] * (n + 1)
        dp[0] = 0 

        # dp[i] denotes the min cost to construct a string of len i
    
        for i in range(n):
            if dp[i] >= 10**10:
                continue
            
            matches = trie.search(target, i)
            #idx denotes the (end index + 1) of prefix string
            #i denotes the start of the substring of target considered
            # or the len of target constructed till now
            # cost is of the prefix
            # We compare whether it is feasible to append the prefix directly 
            # to target of len 'i' or dp[idx] 
            for idx, cost in matches:
                dp[idx] = min(dp[idx], dp[i] + cost)
        
        result = dp[n]
        return result if result < 10**10 else -1

target="abcdef"
words=["abdef","abc","d","def","ef"]
costs=[100,1,1,10,5]
print(Solution.minimumCost(Solution,target,words,costs))