class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        moves = [(0,1),(1,0),(0,-1), (-1,0)]
        fresh, rotten = set(), set()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: fresh.add((r,c))
                elif grid[r][c] == 2: rotten.add((r,c))
                    
        time = 0
        while fresh:
            time += 1
            new = set()
            for row, col in rotten:
                for move in moves:
                    new_move  = row + move[0], col + move[1]
                    if new_move in fresh:
                        new.add(new_move)
                    
            if not new: return -1
            rotten = new
            fresh -= new
            
        return time