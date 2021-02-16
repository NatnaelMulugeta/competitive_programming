class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zeros = len(nums) -  nums.count(0)
        i = 0
        while i < non_zeros:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1

                    