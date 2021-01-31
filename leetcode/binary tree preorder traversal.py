# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return result
           
        # recursive function
        '''
        lst = []
        self.helper(root, lst)
        return lst
    def helper(self, root: TreeNode, lst: List[int]):
        if not root:
            return
        lst.append(root.val)
        self.helper(root.left, lst)
        self.helper(root.right, lst)
        '''