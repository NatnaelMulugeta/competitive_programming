# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = new = ListNode()
        while l1 or l2:
            if l1 and (not l2 or l1.val <= l2.val):
                new.next = ListNode(l1.val)
                l1 = l1.next
            else:
                new.next = ListNode(l2.val)
                l2 = l2.next
            new = new.next

        return head.next
