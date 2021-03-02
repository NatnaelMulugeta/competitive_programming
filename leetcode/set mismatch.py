class Solution:
    def findErrorNums(self, nums: [int]) -> [int]:
        total = sum(nums)
        count = sum(set(nums))
        length = len(nums)
        
        duplicate = total - count
        missing = (length * (length + 1) // 2) - count
        
        return [duplicate, missing]
        

