import bisect

class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        
        return bisect.bisect(nums, target)