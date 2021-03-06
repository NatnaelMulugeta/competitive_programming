# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        node = head
        for _ in range(k):
            if node:
                node = node.next
            else:
                return head

        prev = head
        current = head.next
        for _ in range(1, k):
            if current == None:
                break
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        if prev != None:
            head.next = self.reverseKGroup(current, k)

        return prev