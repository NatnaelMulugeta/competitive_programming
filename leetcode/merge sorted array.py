import bisect
class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        for _ in range(len(nums2)):
            nums1.pop()
            
        for num in nums2:
            bisect.insort(nums1, num)
        
