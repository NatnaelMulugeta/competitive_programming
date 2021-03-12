class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        before, after = 0, len(s)
        
        while (before != after):
            before = len(s)
               
            for char in set(s):
                s = s.replace(char*k, "")
            
            after = len(s)
            
        return s
        
        