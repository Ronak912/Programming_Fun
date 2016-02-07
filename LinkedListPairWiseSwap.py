# http://www.geeksforgeeks.org/pairwise-swap-elements-of-a-given-linked-list-by-changing-links/

# Given a singly linked list, write a function to swap elements pairwise. For example,
# if the linked list is 1->2->3->4->5->6->7 then the function should change it to 2->1->4->3->6->5->7,
# and if the linked list is 1->2->3->4->5->6 then the function should change it to 2->1->4->3->6->5

import SampleLinkedList

def SwapPairs(head):
    if not head:
        return None

    prev = head
    curr = head.next

    head = curr  # point head to the second node

    while True:
        next = curr.next
        curr.next = prev
        if next is None or next.next is None:
            prev.next = next
            break

        prev.next = next.next
        prev = next
        curr = prev.next
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

    ll.list_print(SwapPairs(ll.cur_node))