# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> [int]:
        result = []
        if root == None:
            return result
        node = root
        if node.left:
            result += self.postorderTraversal(node.left)
        if node.right:
            result += self.postorderTraversal(node.right)
        result.append(node.val)
        return result
    
    