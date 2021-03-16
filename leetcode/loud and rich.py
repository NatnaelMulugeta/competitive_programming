from collections import defaultdict
from functools import lru_cache

class Solution:
    def loudAndRich(self, richer: [[int]], quiet: [int]) -> [int]:
        result = []
        graph = defaultdict(list)
        
        for x, y in richer:
            graph[y].append(x)
            
        @lru_cache(maxsize = None, typed = False)
        def dfs(person):
            q = quiet[person]
            
            if person not in graph:
                return person, quiet[person]
            
            for richer in graph[person]:
                new_person, new_q = dfs(richer)
                
                if new_q < q:
                    person = new_person
                    q = new_q
                    
                    
            return person, q
        
        for person in range(len(quiet)):
            result.append(dfs(person)[0])
            
        return result
