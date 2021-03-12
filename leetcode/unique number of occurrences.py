from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: [int]) -> bool:
        count = Counter(arr)
        
        if len(list(count.values())) == len(set(count.values())):
            return True
        
        return False