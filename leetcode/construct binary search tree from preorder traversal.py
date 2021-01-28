# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: [int]) -> TreeNode:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        
        for i in preorder[1:]:
            if i < stack[-1].val:
                new = TreeNode(i)
                stack[-1].left = new
                stack.append(new)
            else:
                while stack and i > stack[-1].val:
                    node = stack.pop()
                new = TreeNode(i)
                node.right = new
                stack.append(new)
                
        return root
    