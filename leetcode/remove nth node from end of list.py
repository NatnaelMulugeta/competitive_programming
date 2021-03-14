# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = head
        
        result = prev = ListNode()
        prev.next = head
        
        for _ in range(n-1):
            fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
            prev = prev.next
            
        prev.next = slow.next
        return result.next