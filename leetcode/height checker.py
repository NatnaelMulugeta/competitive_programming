class Solution:
    def heightChecker(self, heights: [int]) -> int:
        ordered = sorted(heights)
        change = 0
        for i in range(len(heights)):
            if heights[i] != ordered[i]:
                change += 1
                
        return change