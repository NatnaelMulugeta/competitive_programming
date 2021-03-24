class Solution:
    def maxJumps(self, arr: [int], d: int) -> int:
        result = 1
        
        all_moves = [0] * len(arr)
        
        def dfs(index):
            moves = 1
            
            for i in range(index+1, min(len(arr), index+d+1)):
                if arr[i] >= arr[index]:
                    break
                    
                if not all_moves[i]: 
                    dfs(i)
                    
                moves = max(moves, all_moves[i]+1)
                
            for i in reversed(range(max(0, index-d), index)):
                if arr[i] >= arr[index]:
                    break
                    
                if not all_moves[i]:
                    dfs(i)
                    
                moves = max(moves, all_moves[i]+1)
                
            all_moves[index] = moves
            
            
        for i in range(len(arr)):
            if not all_moves[i]: dfs(i)
                
            result = max(result, all_moves[i])
        

        return result
