from collections import Counter

class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        result = []
                
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        for num in nums1:
            if num in count1 and num in count2:
                if count1[num] > 0 and count2[num] > 0:
                    count1[num] -= 1
                    count2[num] -= 1
                    result.append(num)
                
        return result