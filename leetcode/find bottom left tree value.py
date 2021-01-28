# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return None
        if not root.left and not root.right:
            return root.val
        
        stack = [(root, 0)]
        height = 0
        while stack:
            node, h = stack.pop(0)
            if h > height:
                left = node
                height = h
            
            if node.left:
                stack.append((node.left, h+1))
            if node.right:
                stack.append((node.right, h+1))
                
        return left.val
    