# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, root, low, high):
        if not root:
            return True
        
        if root.val <= low or root.val>= high:
            return False
        
        left = self.helper(root.left, low, root.val)
        right = self.helper(root.right, root.val, high)
        
        return left and right