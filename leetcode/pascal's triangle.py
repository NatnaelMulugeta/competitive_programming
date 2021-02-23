class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for row in range(numRows):
            curr_row = [1 for _ in range(row+1)]
            for i in range(1, len(curr_row)-1):
                curr_row[i] = result[row-1][i-1] + result[row-1][i]
                
            result.append(curr_row)
        
        return result
            