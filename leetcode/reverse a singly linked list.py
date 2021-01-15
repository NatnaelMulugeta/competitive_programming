# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        lst = head.next
        rev_lst = head
        rev_lst.next = None
        while lst != None:
            lst1 = lst
            lst = lst.next
            lst1.next = rev_lst
            rev_lst = lst1

        return rev_lst