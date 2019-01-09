#http://www.geeksforgeeks.org/swap-nodes-in-a-linked-list-without-swapping-data/

# Swap nodes in a linked list without swapping data
#
# Input:  10->15->12->13->20->14,  x = 12, y = 20
# Output: 10->15->20->13->12->14
#
# Input:  10->15->12->13->20->14,  x = 10, y = 20
# Output: 20->15->12->13->10->14
#
# Input:  10->15->12->13->20->14,  x = 12, y = 13
# Output: 10->15->13->12->20->14
#
# This may look a simple problem, but is interesting question as it has following cases to be handled.
# 1) x and y may or may not be adjacent.
# 2) Either x or y may be a head node.
# 3) Either x or y may be last node.
# 4) x and/or y may not be present in linked list.

import SampleLinkedList

def swap(head, first, second):
    if first == second:
        return None

    headnode = head

    prevx = None
    currx = headnode

    while currx and currx.data != first:
        prevx = currx
        currx = currx.next

    prevy = None
    curry = headnode
    while curry and curry.data != second:
        prevy = curry
        curry = curry.next

    if not prevx:
        headnode = curry
    else:
        prevx.next = curry

    if not prevy:
        headnode = currx
    else:
        prevy.next = currx

    temp = currx.next
    currx.next = curry.next
    curry.next = temp

    return headnode

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

    head = swap(ll.cur_node, 4, 7)

    ll.list_print(head)
