from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges: [[int]], hasApple: [bool]) -> int:
        graph = defaultdict(list)
        
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        def dfs(node, visited):
            nonlocal result
			
            apple = False    
            if hasApple[node]:
                apple = True
                
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    curr = dfs(neighbour, visited)
                    if curr: apple = apple or curr
            
            if node and apple:
                result += 2
			
            return apple
        
        result = 0
        dfs(0, {0})
        
        return result