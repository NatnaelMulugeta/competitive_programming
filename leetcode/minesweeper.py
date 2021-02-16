from collections import deque

class Solution:
    def updateBoard(self, board: [[str]], click: [int]) -> [[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        def bound(move):
            return 0 <= move[0] < len(board) and 0 <= move[1] < len(board[0])
        
        queue = deque( [ tuple(click) ] )
        visited = set( [ tuple(click) ] )
        moves = [(1,0), (0,1), (1,1), (-1,0), (0,-1), (-1,-1), (1,-1), (-1,1)]
        
        while queue:
            node = queue.popleft()
            
            bombs = 0
            current_queue = []
            
            for move in moves:
                new_move = node[0] + move[0], node[1] + move[1]
                
                if bound(new_move) and new_move not in visited:
                    current_queue.append(new_move)
                    
                    bombs += 1 if board[new_move[0]][new_move[1]] == 'M' else 0
            
            if not bombs:
                for cell in current_queue:
                    queue.append(cell)
                    visited.add(cell)
                    
            board[node[0]][node[1]] = 'B' if not bombs else str(bombs)
            
        return board
                    
