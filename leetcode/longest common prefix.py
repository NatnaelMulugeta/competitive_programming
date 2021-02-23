class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if len(strs) == 0:
            return ""
        
        strs.sort()
        first, last = strs[0], strs[-1]
        
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
            
        return first[:i]