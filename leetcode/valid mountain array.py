class Solution:
    def validMountainArray(self, arr: [int]) -> bool:
        if len(arr) < 3:
            return False
        
        inc = True
        
        if arr[0] > arr[1] or arr[-1] > arr[-2]: return False
        
        for i in range(len(arr)-1):
            if inc:
                if arr[i] < arr[i+1]: continue
                elif arr[i] > arr[i+1]: inc = not inc
                else: return False
            else:
                if arr[i] > arr[i+1]: continue
                else: return False
        
        return True
        