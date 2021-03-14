from collections import defaultdict

class Solution:
    def findCenter(self, edges: [[int]]) -> int:
        graph = defaultdict(int)
        
        for edge in edges:
            graph[edge[0]] += 1
            graph[edge[1]] += 1
            
        for key, val in zip(graph.keys(), graph.values()):
            if val == len(edges):
                return key