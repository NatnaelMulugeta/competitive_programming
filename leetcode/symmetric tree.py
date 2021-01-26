# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        node = root
        if node == None:
            return True
        nodes_lst = [node.left, node.right]
        while nodes_lst:
            right = nodes_lst.pop()
            left = nodes_lst.pop()
            if left == None and right == None:
                continue
            elif left == None or right == None:
                return False
            elif left != None and right != None:
                if left.val != right.val:
                    return False
                nodes_lst.append(left.right)
                nodes_lst.append(right.left)
                nodes_lst.append(left.left)
                nodes_lst.append(right.right)
                
        return True                
            