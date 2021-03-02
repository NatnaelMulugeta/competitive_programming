class Solution:
    def maxArea(self, height: [int]) -> int:
        area = 0
        
        left, right = 0, len(height) - 1
        length = 0
        
        while left < right:
            width = right - left
            
            if height[left] < height[right]:
                length = height[left]
                left += 1
            else:
                length = height[right]
                right -= 1
                
            area = max([area, length * width])
                

        return area