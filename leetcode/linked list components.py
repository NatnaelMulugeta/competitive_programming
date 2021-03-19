# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: ListNode, G: [int]) -> int:
        result = 0
        
        g = set(G)
        node = head
        while node:
            if node.val in g:
                
                temp = node.next
                if temp == None or temp.val not in g:
                    result += 1
            
            node = node.next
            
        return result
        
