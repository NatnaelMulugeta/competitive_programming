def findMergeNode(head1, head2):
    h1, h2 = head1, head2
    len1, len2 = 0, 0
    while h1 != None:
        len1 += 1
        h1 = h1.next
    while h2 != None:
        len2 += 1
        h2 = h2.next
    
    if len2 > len1:
        len1, len2 = len2, len1
        head1, head2 = head2, head1
    for i in range(len1 - len2):
        head1 = head1.next

    while head1 != None and head2 != None:
        if head1 == head2:
            return head1.data
        head1 = head1.next
        head2 = head2.next