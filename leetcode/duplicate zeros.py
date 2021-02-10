class Solution:
    def duplicateZeros(self, arr: [int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        l = len(arr)
        while i < l:
            if arr[i] == 0:
                arr.insert(i+1, 0)
                i += 1
            i += 1
            
        for i in range(len(arr), l, -1):
            arr.pop()
            
        
