class Solution:
    def replaceElements(self, arr: [int]) -> [int]:
        if len(arr) < 2: return [-1]
        
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])
        
        arr[-1] = -1
        
        return arr
        