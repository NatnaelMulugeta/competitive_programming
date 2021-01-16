def has_cycle(head):
    slow = head
    fast = head.next
    
    if head == None:
        return 0
    
    while slow != fast:
        if fast == None or fast.next == None:
            return 0
        slow = slow.next
        fast = fast.next.next
        
    return 1