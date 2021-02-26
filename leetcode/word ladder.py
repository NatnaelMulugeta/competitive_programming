from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: [str]) -> int:
        graph = defaultdict(list)
        visited = set()
        
        if endWord not in wordList:
            return 0
        
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + " " + word[i+1:]
                graph[key].append(word)
                
                
        queue = deque([(beginWord, 1)])
        while queue:
            word, step = queue.popleft()
            
            if word == endWord:
                return step
            
            if word in visited:
                continue
            visited.add(word)
            
            
            for i in range(len(word)):
                key = word[:i] + " " + word[i+1:]
                for next_word in graph[key]:
                    queue.append((next_word, step+1))

        return 0