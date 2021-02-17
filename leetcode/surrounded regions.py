from collections import deque

class Solution:
    # BFS
    
    def solve(self, board: [[str]]) -> None:
        if len(board) == 0 or len(board[0]) == 0:
            return

        def bound(move):
            return 0 <= move[0] < row and 0 <= move[1] < col
        
        row = len(board)
        col = len(board[0])
        
        zero_borders = deque()
        moves = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()
        
        for r in range(row):
            if board[r][0] == 'O':
                zero_borders.append((r,0))
            if board[r][col-1] == 'O':
                zero_borders.append((r,col-1))
        
        
        for c in range(col-2):
            if board[0][c+1] == 'O':
                zero_borders.append((0,c+1))
            if board[row-1][c+1] == 'O':
                zero_borders.append((row-1,c+1))
                
        # print(zero_borders)
        
        while zero_borders:
            node = zero_borders.popleft()
            visited.add(node)
            
            for move in moves:
                new_move = node[0] + move[0], node[1] + move[1]
                if bound(new_move) and new_move not in visited:
                    if board[new_move[0]][new_move[1]] == 'O':
                        zero_borders.append(new_move)
                        visited.add(new_move)
                        
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O' and (r,c) not in visited:
                    board[r][c] = 'X'
    
    
    
    # DFS
    
#     def bound(self,move,row,col):
#             return 0 <= move[0] < row and 0 <= move[1] < col
        
#     def solve(self, board: List[List[str]]) -> None:
#         if len(board) == 0 or len(board[0]) == 0:
#             return
                
#         row = len(board)
#         col = len(board[0])
#         visited = set()
        
#         for r in range(row):
#             for c in range(col):
#                 if((r == 0 or r == row - 1 or c == 0 or c == col - 1) and board[r][c] == "O"):
#                     visited.add((r,c))
#                     self.dfs((r,c),board,visited,row,col)
        
#         for r in range(row):
#             for c in range(col):
#                 if board[r][c] == "O" and (r,c) not in visited:
#                     board[r][c] = "X"
    
#     def dfs(self,cell,board,visited,row,col):
#         directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
#         for direction in directions:
#             new_cell = nx,ny = cell[0] + direction[0],cell[1] + direction[1]
#             if self.bound(new_cell,row,col) and board[nx][ny] == "O" and new_cell not in visited:
#                 visited.add(new_cell)
#                 self.dfs(new_cell,board,visited,row,col)
                
        
