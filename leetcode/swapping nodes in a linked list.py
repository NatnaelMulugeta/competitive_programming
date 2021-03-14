# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        slow = head
        fast = head
        
        for _ in range(k-1):
            fast = fast.next
        left = fast
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        right = slow
        
        left.val, right.val = right.val, left.val
        
        return head
        