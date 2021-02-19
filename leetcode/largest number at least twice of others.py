class Solution:
    def dominantIndex(self, nums: [int]) -> int:
        largest = max(nums)
        i = nums.index(largest)
        
        for num in nums:
            if 2*num > largest and num < largest:
                return -1
            
        return i
    