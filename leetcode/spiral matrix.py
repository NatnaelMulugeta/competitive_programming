class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if not matrix:
            return []
        
        def bound(r, c):
            return 0 <= r < row and 0 <= c < col
        
        result = []
        
        row = len(matrix)
        col = len(matrix[0])
        visited = [[False] * col for _ in matrix]
        
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        
        r, c = 0, 0
        move = 0
        for _ in range(row * col):
            result.append(matrix[r][c])
            visited[r][c] = True
            curr_row, curr_col  = r + moves[move][0], c + moves[move][1]
            if bound(curr_row, curr_col) and not visited[curr_row][curr_col]:
                r, c = curr_row, curr_col
            else:
                move = (move + 1) % 4
                r, c = r + moves[move][0], c + moves[move][1]
                
        return result
        
        