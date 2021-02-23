class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        nums[:] = nums[(len(nums) - k):] + nums[:(len(nums) - k)]