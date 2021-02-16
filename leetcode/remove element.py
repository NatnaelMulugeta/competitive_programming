class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        for num in nums[:]:
            if num == val:
                nums.remove(val)
        return len(nums)
            