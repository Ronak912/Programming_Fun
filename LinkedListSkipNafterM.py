# http://www.geeksforgeeks.org/delete-n-nodes-after-m-nodes-of-a-linked-list/

# Delete N nodes after M nodes of a linked list
# Given a linked list and two integers M and N.
# Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same till end of the linked list.
#
# Input:
# M = 2, N = 2
# Linked List: 1->2->3->4->5->6->7->8
# Output:
# Linked List: 1->2->5->6

import SampleLinkedList


def skipMAfterN(head, m, n):
    curr = head

    while curr:
        for i in xrange(0, m-1):
            curr = curr.next
            if curr is None:
                break

        t = curr
        for i in xrange(0, n):
            t = t.next
            if t is None:
                return

        curr.next = t.next
        curr = curr.next
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
    ll.add_node(9)
    ll.add_node(10)

    ll.list_print(skipMAfterN(ll.cur_node, 2, 2))