class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ops = 0
        for log in logs:
            if log == "../":
                ops = max(0, ops-1)
            elif log != "./":
                ops += 1
        return ops
        