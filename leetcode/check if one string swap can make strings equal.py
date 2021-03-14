class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True

        lst1, lst2 = [], []
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                lst1.append(s1[i])
                lst2.append(s2[i])
                
        if len(lst1) == len(lst2) == 2:
            if lst1[0] == lst2[1] and lst1[1] == lst2[0]:
                return True
            
        return False
    