from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: [[int]], blue_edges: [[int]]) -> [int]:
        
        result = [0] + [-1] * (n - 1)
        graph = defaultdict(list)
        visited = set()
        
        for node1, node2 in red_edges:
            graph[node1].append([node2, "r"])
            
        for node1, node2 in blue_edges:
            graph[node1].append([node2, "b"])
            
        queue = deque()
        for node, color in graph[0]:
            queue.append([node, color, 1])
            
        while queue:
            node, color, step = queue.popleft()
            
            if result[node] == -1: result[node] = step
                
            if (node, color) not in visited:
                visited.add((node, color))
                
                for next_node, next_color in graph[node]:
                    if next_color != color and (next_node, next_color) not in visited:
                        queue.append([next_node, next_color, step + 1])
                        
        return result
            
