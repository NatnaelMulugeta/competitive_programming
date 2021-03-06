class Solution:
    def search(self, nums: [int], target: int) -> int:
        hashset = set(nums)
        
        if target in hashset:
            return nums.index(target)
        
        return -1