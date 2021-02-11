class Solution:
    def maxAreaOfIsland(self, grid: [[int]]) -> int:
        max_area = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(max_area, self.areaIfLand(grid, row, col))
                    
        return max_area
        
        
    def areaIfLand(self, grid: [[int]], row: int, col: int) -> int:
        grid[row][col] = 0
        
        area = 1
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for r, c in directions:
            curr_row, curr_col = row + r, col + c
            if 0 <= curr_row < len(grid) and 0 <= curr_col < len(grid[0]) and grid[curr_row][curr_col] == 1:
                area += self.areaIfLand(grid, curr_row, curr_col)
                
        return area
        
