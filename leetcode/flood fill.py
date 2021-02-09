class Solution:
    def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) -> [[int]]:
        
        start_color = image[sr][sc]
        if start_color == newColor:
            return image
        
        stack = [(sr, sc)]
        row, col = len(image), len(image[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while stack:
            curr_row, curr_col = stack.pop()

            if curr_row < 0 or curr_col < 0 or curr_row >= row or curr_col >= col: continue
            if image[curr_row][curr_col] != start_color: continue
            
            image[curr_row][curr_col] = newColor
            
            for r, c in directions:
                stack.append((curr_row + r, curr_col + c))
                
        return image
       