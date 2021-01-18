
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index >= self.size:
            return -1
        current = self.head
        node = ListNode(val)
        if index <= 0:
            node.next = current
            self.head = node
        else:
            for _ in range(index-1):
                current = current.next
            node.next = current.next
            current.next = node
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(index-1):
                current = current.next
            current.next = current.next.next
        self.size -= 1
