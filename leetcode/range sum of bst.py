# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root == None:
            return 0
        node = root
        node_sum = 0
        if node.val >= low and node.val <= high:
            node_sum += node.val
        if low < node.val:
            node_sum += self.rangeSumBST(node.left, low, high)
        if high > node.val:
            node_sum += self.rangeSumBST(node.right, low, high)
            
        return node_sum

        