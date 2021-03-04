class Solution:
    def missingNumber(self, nums: [int]) -> int:
        hashset = set(nums)
        for i in range(len(nums) + 1):
            if i not in hashset:
                return i