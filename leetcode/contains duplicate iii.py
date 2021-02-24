class Solution:
    def containsNearbyAlmostDuplicate(self, nums: [int], k: int, t: int) -> bool:
        hashmap = []
        for i, num in enumerate(nums):
            hashmap.append([num,i])
            
        hashmap.sort(key = lambda elem: elem[0])
        
        for i in range(len(hashmap)):
            for j in range(i+1,len(hashmap)):
                if abs(hashmap[i][0] - hashmap[j][0]) > t:
                    break
                elif abs(hashmap[i][1]-hashmap[j][1]) <= k:
                    return True
        
        return False