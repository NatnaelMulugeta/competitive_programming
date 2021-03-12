class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        length = 0
        
        i, j = 0, 0
        cost = 0
        while i < len(s):
            curr = abs(ord(t[i]) - ord(s[i]))
            cost += curr
            while cost > maxCost:
                cost -= abs(ord(t[j]) - ord(s[j]))
                j += 1
                
            length = max(length, 1+i-j)
            
            i += 1
        
        return length
  
           