class Solution:
    def thirdMax(self, nums: [int]) -> int:
        ordered = sorted(nums, reverse = True)
        
        if len(nums) < 3: return ordered[0]
        
        i, third = 1, 1
        while third <= 3:
            if i == len(nums):
                break
                
            if ordered[i] != ordered[i-1]: third += 1
            
            if third == 3:
                return ordered[i]
            
            i += 1
            
        return ordered[0]
        