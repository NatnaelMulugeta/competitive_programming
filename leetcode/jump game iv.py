from collections import defaultdict
from collections import deque

class Solution:
    def minJumps(self, arr: [int]) -> int:
        
        def bound(index):
            return 0 <= index < len(arr)
        
        graph = defaultdict(list)
        
        for i, v in enumerate(arr):
            graph[v].append(i)
            
        queue = deque([(0, 0)])
        visited = set()
        
        while queue:
            index, step = queue.popleft()
            
            if index == len(arr) - 1:
                return step
            
            if index not in visited:
                visited.add(index)
                
                if bound(index-1) and index - 1 not in visited:
                    queue.append((index-1, step+1))
                
                if bound(index+1) and index + 1 not in visited:
                    queue.append((index+1, step+1))
                 
                for i in graph[arr[index]]:
                    if i not in visited:
                        queue.append((i, step + 1))     
                        
                del graph[arr[index]]
                
                    
        return -1
                      