class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_two_nums(l1, l2):
        n1 = l1
        n2 = l2
        lst1 = []
        lst2 = []

        while n1:
            lst1.append(n1.val)
            n1 = n1.next
        while n2:
            lst2.append(n2.val)
            n2 = n2.next

        lst1.reverse()
        lst2.reverse()
        num1 = int("".join(str(x) for x in lst2))
        num2 = int("".join(str(x) for x in lst2))

        result = list(str(num1 + num2))
        head = l3 = ListNode(result.pop())
        result.reverse()

        for i in result:
            l3.next = ListNode(i)
            l3 = l3.next

        return head


  
