class Solution:
    def canReach(self, arr: [int], start: int) -> bool:
        visited = set()
        
        stack = [start]
        while stack:
            curr = stack.pop()
            if arr[curr] == 0:
                return True
            visited.add(curr)
            
            index1 = curr + arr[curr]
            index2 = curr - arr[curr]
            
            if index1 not in visited and 0 <= index1 < len(arr):
                stack.append(index1)
            if index2 not in visited and 0 <= index2 < len(arr):
                stack.append(index2)
                
        return False
                
    