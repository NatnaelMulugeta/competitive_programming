from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: [str]) -> str:
        result = ""
        
        for c in ",.;!?'": 
            paragraph = paragraph.replace(c, " ")
        
        words = [word.lower() for word in paragraph.split()]
        words_count = Counter(words)
        count = 0
        
        for word in words:
            if word not in set(banned) and words_count[word] > count:
                count = words_count[word]
                result = word
                    
                    
        return result
            
        
