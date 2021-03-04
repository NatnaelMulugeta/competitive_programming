class Solution:
    def kSmallestPairs(self, nums1: [int], nums2: [int], k: int) -> [[int]]:
        k_pairs = []
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                k_pairs.append([nums1[i],nums2[j]])
                
        k_pairs.sort(key = lambda pair: pair[0] + pair[1])
        
        return k_pairs[:k]
            