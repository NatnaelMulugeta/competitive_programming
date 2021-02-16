# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        node = root
        left = self.minDepth(node.left)
        right = self.minDepth(node.right)
        
        if not(left and right):
            return left + right + 1
        else:
            return min(left, right) + 1