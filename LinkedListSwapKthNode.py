# http://www.geeksforgeeks.org/swap-kth-node-from-beginning-with-kth-node-from-end-in-a-linked-list/

# Swap Kth node from beginning with Kth node from end in a Linked List
#
# Following are the interesting cases that must be handled.
# 1) Y is next to X
# 2) X is next to Y
# 3) X and Y are same
# 4) X and Y do not exist (k is more than number of nodes in linked list)

import SampleLinkedList

def getLengthOfcount(head):
    curr = head
    count = 1
    while curr.next:
        curr = curr.next
        count += 1
    return count

def swapKthNode(head, k):
    n = getLengthOfcount(head)

    if k > n:
        return 'position is great than total size'

    if 2*k - 1 == n:
        return 'This is same element'

    xprev = None
    xcurr = head
    for idx in xrange(1, k):
        xprev = xcurr
        xcurr = xcurr.next

    yprev = None
    ycurr = head
    for idx in xrange(1, n-k+1):
        yprev = ycurr
        ycurr = ycurr.next

    if xprev is not None:
        xprev.next = ycurr

    if yprev is not None:
        yprev.next = xcurr

    tmpx = xcurr.next
    xcurr.next = ycurr.next
    ycurr.next = tmpx

    # Change head pointers when k is 1 or n
    if k == 1:
        head = ycurr
    elif k == n:
        head = xcurr

    return head

if __name__ == '__main__':
    ll = SampleLinkedList.LinkedList()

    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(4)
    ll.add_node(5)
    ll.add_node(6)
    ll.add_node(7)
    ll.add_node(8)

    ll.list_print(swapKthNode(ll.cur_node, 8))