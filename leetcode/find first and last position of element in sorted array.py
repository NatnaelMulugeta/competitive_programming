class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        result = [-1,-1]
        if not nums:
            return result
        
        left, right = 0, len(nums)-1
        start = self.searchBinary(nums, target, left, right, True)
        if start >= len(nums) or nums[start] != target:
            return result
        result[0] = start
        result[1] = self.searchBinary(nums, target, left, right, False)
        return result
    
    
    def searchBinary(self, nums: [int], target: int, left: int, right: int, start: bool) -> int:
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    if start:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                
            if start:
                return left
            return right