class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        matrix = [[0] * n for _ in range(n)]
        
        def bound(r, c):
            return 0 <= r < n and 0 <= c < n
        
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        
        r, c = 0, 0
        move = 0
        for num in range(n*n):
            matrix[r][c] = num + 1
            curr_row, curr_col = r + moves[move][0], c + moves[move][1]
            if bound(curr_row, curr_col) and matrix[curr_row][curr_col] == 0:
                r, c = curr_row, curr_col
            else:
                move = (move + 1) % 4
                r, c = r + moves[move][0], c + moves[move][1]
                
        return matrix