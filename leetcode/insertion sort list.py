# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        head = ListNode(float('-inf'), head)
        h = head
        while h.next:
            if h.next.val < h.val:
                node, temp = h.next, h.next.next
                h.next = temp
                self.insertNode(head, node)
            else:
                h = h.next
        return head.next

    def insertNode(self, head: ListNode, node: ListNode) -> ListNode:
        while head.next:
            if node.val <= head.next.val:
                node.next, head.next = head.next, node
                break
            head = head.next
