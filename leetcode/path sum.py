# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        return self.helper(root, 0, targetSum)
        
    def helper(self, root: TreeNode, node_sum: int, targetSum: int) -> bool:
        if not root:
            return False
        
        node_sum += root.val
        if not root.left and not root.right and node_sum == targetSum:
            return True
        
        return self.helper(root.left, node_sum, targetSum) or self.helper(root.right, node_sum, targetSum)
        