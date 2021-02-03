import heapq

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        heap = []
        head = ListNode()
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i))
                
        node = head
        while heap:
            curr, i = heapq.heappop(heap)
            node.next = ListNode(curr)
            node = node.next
            
            if lists[i]:
                lists[i] = lists[i].next
                if lists[i]:
                    heapq.heappush(heap, (lists[i].val, i))
        
        return head.next