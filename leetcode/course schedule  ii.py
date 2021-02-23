from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        result = []
        
        indegree = [0] * numCourses
        for node in prerequisites:
            indegree[node[0]] += 1
            
        if 0 not in indegree:
            return []
        
        queue = deque()
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            course = queue.popleft()
            for pre in prerequisites:
                if pre[1] == course:
                    indegree[pre[0]] -= 1
                    if indegree[pre[0]] == 0:
                        queue.append(pre[0])
                        
            result.append(course)
                        
        return result if not any(indegree) else []