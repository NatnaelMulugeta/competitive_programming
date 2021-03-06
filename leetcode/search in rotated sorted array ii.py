class Solution:
    def search(self, nums: [int], target: int) -> bool:
        hashset = set(nums)
        
        if target in hashset:
            return True
        
        return False