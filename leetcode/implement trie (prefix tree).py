from collections import defaultdict

class TrieNode:
    
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        
        for w in word:
            curr = curr.children[w]
            
        curr.word = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        
        for w in word:
            curr = curr.children.get(w)
            
            if not curr: return False
        
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for p in prefix:
            curr = curr.children.get(p)
            
            if not curr: return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)