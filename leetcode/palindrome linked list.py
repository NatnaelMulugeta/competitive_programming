# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        lst = []
        while head:
            lst.append(head)
            head = head.next
        for i in lst:
            if i != lst.pop():
                reurn False
        return True