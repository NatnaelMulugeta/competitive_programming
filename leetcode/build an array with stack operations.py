class Solution:
    def buildArray(self, target: [int], n: int):
        result = []
        i, idx = 1, 0
        while i <= n:
            if idx == len(target):
                break
            if i == target[idx]:
                result.append("Push")
                idx += 1
            else:
                result.append("Push")
                result.append("Pop")
            i += 1
        return result
