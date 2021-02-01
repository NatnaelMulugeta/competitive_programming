import math
class Solution:
    def smallestDivisor(self, nums: [int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            d = left + (right-left)//2
            s = sum(math.ceil(i/d) for i in nums)
            if s > threshold:
                left = d + 1
            else:
                right = d
                
        return right
