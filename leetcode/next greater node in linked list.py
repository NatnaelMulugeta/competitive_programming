# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def nextLargerNodes(self, head: ListNode):
        if head == None or head.next == None:
            return [0]
        result, stack = [], []
        while head:
            while stack and stack[-1][1] < head.val:
                result[stack.pop()[0]] = head.val
            stack.append([len(result), head.val])
            result.append(0)
            head = head.next
        return result
