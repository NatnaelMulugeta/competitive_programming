# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            new = TreeNode(val)
            return new
        node = root
        if node.val < val:
            node.right = self.insertIntoBST(node.right, val)
        elif root.val > val:
            node.left = self.insertIntoBST(node.left, val)
        
        return node
        