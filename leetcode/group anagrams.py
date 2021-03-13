from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        words = defaultdict(list)
        
        for word in strs:
            key = tuple(sorted(word))
    
            words[key].append(word)
            
        return words.values()