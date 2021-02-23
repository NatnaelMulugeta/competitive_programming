from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: [[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        if grid[0][0] != 0 or grid[rows-1][cols-1] != 0:
            return -1
        
        moves = [(1,0), (0,1), (-1,0), (0,-1), (-1,-1), (-1,1), (1,-1), (1,1)]
        visited = set()
        
        def bound(move):
            return 0 <= move[0] < rows and 0 <= move[1] < cols
        
        
        queue = deque([(0,0)])
        visited.add((0,0))
        distance = 0
        while queue:
            distance += 1
            length = len(queue)
            while length > 0:
                length -= 1
                
                cell = queue.popleft()
                if cell == (rows-1, cols-1):
                    return distance
            
                for move in moves:
                    new_move = r, c= cell[0] + move[0], cell[1] + move[1]
                    if bound(new_move) and new_move not in visited and grid[r][c] == 0:
                        queue.append(new_move)
                        visited.add(new_move)
            
        return -1