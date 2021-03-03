from collections import deque

class Solution:
    def highestPeak(self, isWater: [[int]]) -> [[int]]:
        
        def bound(move):
            return 0 <= move[0] < len(isWater) and 0 <= move[1] < len(isWater[0])
        
        visited = set()
        queue = deque()
        moves = [(1,0), (0,1), (-1,0), (0,-1)]
        
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    isWater[i][j] = 0
                    queue.append((i,j))
                    visited.add((i,j))
       
        while queue:
            curr = row, col = queue.popleft()
            for move in moves:
                new = row + move[0], col + move[1]
                
                if bound(new) and new not in visited:
                    isWater[new[0]][new[1]] = isWater[row][col] + 1
                    visited.add(new)
                    queue.append(new)
            
            
        return isWater