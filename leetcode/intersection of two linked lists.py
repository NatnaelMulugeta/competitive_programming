# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        len1, len2 = 0, 0
        
        while a != None:
            len1 += 1
            a = a.next
            
        while b != None:
            len2 += 1
            b = b.next
            
        if len2 > len1:
            len1, len2 = len2, len1
            headA, headB = headB, headA
            
        for _ in range(len1 - len2):
            headA = headA.next
            
        while headA != None and headB != None:
            if headA == headB:
                return headA
            
            headA = headA.next
            headB = headB.next
            
        return