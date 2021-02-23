class Solution:
    def maxDistance(self, grid: [[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def bound(move):
            return 0 <= move[0] < rows and 0 <= move[1] < cols
        
        lands = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: lands.add((r,c))
            
        visited = len(lands)
        if visited == 0 or visited == rows*cols:
            return -1
        
        distance = 0
        while visited < rows*cols:
            new = set()
            
            for r, c in lands:
                for move in moves:
                    new_move = i, j = r + move[0], c + move[1]
                    if not bound(new_move): continue
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                        visited += 1
                        new.add(new_move)
                        
            distance += 1
            lands = new
            
        return distance