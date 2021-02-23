class Solution:
    def minSubArrayLen(self, target: int, nums: [int]) -> int:
        start, total = 0, 0
        result = float('inf')
        
        for i in range(len(nums)):
            total += nums[i]
            
            while total >= target:
                result = min(result, i-start+1)
                total -= nums[start]
                start += 1
                
        return result if result != float('inf') else 0