class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        words = s.split()
        
        for w in words:
            result += w[::-1] + " "
            
        return result.strip()