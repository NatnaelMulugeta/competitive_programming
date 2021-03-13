class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        boxs = [{} for _ in range(9)]
        
        for row_index in range(9):
            for col_index in range(9):
                num = board[row_index][col_index]
                
                if num != ".":
                    box_index = row_index // 3 * 3 + col_index // 3
                    
                    rows[row_index][num] = rows[row_index].get(num, 0) + 1
                    cols[col_index][num] = cols[col_index].get(num, 0) + 1
                    boxs[box_index][num] = boxs[box_index].get(num, 0) + 1
                    
                    if rows[row_index][num] > 1 or cols[col_index][num] > 1 or boxs[box_index][num] > 1: 
                        return False
                    
        return True
        
                