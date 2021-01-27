from collections import Counter
class Solution:
    def frequencySort(self, nums: [int]) -> [int]:
        count = Counter(nums)
        result = []
        while count:
            key = nums[0]
            val = count[nums[0]]
            for k, v in count.items():
                if v < val:
                    val, key = v, k
                elif v == val:
                    if k > key:
                        key = k
            for _ in range(val):
                result.append(key)
                nums.remove(key)
            del count[key]
        
        return result
        
        
obj = Solution()
print(obj.frequencySort([1,2,1,1,0,2,3]))