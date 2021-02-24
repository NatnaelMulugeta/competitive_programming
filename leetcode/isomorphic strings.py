class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap.keys():
                if t[i] not in hashmap.values():
                    hashmap[s[i]] = t[i]
                else:
                    return False
            elif hashmap[s[i]] != t[i]:
                return False
            
        return True
                