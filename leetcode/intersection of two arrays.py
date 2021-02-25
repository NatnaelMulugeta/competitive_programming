class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        result = set()
                
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        set1 = set(nums1)
        set2 = set(nums2)
        
        for num in nums1:
            if num in set1 and num in set2:
                result.add(num)
                
        return list(result)
        