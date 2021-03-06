class Solution:
    def minimumLengthEncoding(self, words: [str]) -> int:
        chars = set(words)
        for word in words:
            for k in range(1, len(word)):
                chars.discard(word[k:])

        return sum(len(word) + 1 for word in chars)
        