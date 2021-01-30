class Solution:
    def countNegatives(self, grid: [[int]]) -> int:
        count = 0
        row, col = len(grid) -1, 0
        while row >= 0 and col < len(grid[0]):
            if grid[row][col] < 0:
                row -= 1
                count += len(grid[0]) - col
            else:
                col += 1
        
        return count
                