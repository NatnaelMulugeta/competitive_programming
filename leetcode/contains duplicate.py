class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        elems = set()
        for num in nums:
            if num in elems:
                return True
            elems.add(num)
            
        return False