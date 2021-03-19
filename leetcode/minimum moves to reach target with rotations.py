from collections import deque

class Solution:
    def minimumMoves(self, grid: [[int]]) -> int:
        
        def bound(head, tail):
            return 0 <= head[0] < len(grid) and 0 <= head[1] < len(grid) and 0 <= tail[0] < len(grid) and 0 <= tail[1] < len(grid)
        
        def possible(head, tail):
            return grid[head[0]][head[1]] == 0 and grid[tail[0]][tail[1]] == 0
        
        def rotate(head, tail, index):
            if index == 2: 
                return head[1] == tail[1] and grid[head[0]][head[1]+1] == 0
            elif index > 2:
                return head[0] == tail[0] and grid[head[0]+1][head[1]] == 0
            elif index < 2:
                return True
        
        start = ((0,1), (0,0))
        end = ((len(grid)-1, len(grid)-1), (len(grid)-1, len(grid)-2))
        
        visited = {start}
        
        moves = [((0,1), (0, 1)), ((1, 0), (1, 0)), ((1, -1), (0, 0)), ((-1, 1), (0, 0))]
        
        queue = deque([((0,1), (0,0), 0)])
        
        while queue:
            head, tail, step = queue.popleft()
            
            if head == end[0] and tail == end[1]: return step
            
            for i, (h_move, t_move) in enumerate(moves):
                new_h = head[0] + h_move[0], head[1] + h_move[1]
                new_t = tail[0] + t_move[0], tail[1] + t_move[1]
                # if bound(new_h, new_t): print(f'{new_h=}, {new_t=}, {i=}: {rotate(new_h, new_t, i)=}')
                if bound(new_h, new_t) and possible(new_h, new_t) and rotate(new_h, new_t, i) and (new_h, new_t) not in visited:
                    
                    queue.append((new_h, new_t, step+1))
                    # print(new_h, new_t, step + 1)
                    visited.add((new_h, new_t))
                    
        return -1
        