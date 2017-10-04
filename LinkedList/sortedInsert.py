# http://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/

# Insert value in sorted LinkedList

import LinkedList


def sortedInsert(ll, newnode):

    head = ll.cur_node
    if head is None or head.data > newnode.data:
        newnode.next = head
        ll.cur_node = newnode
    else:
        currnode = head
        while currnode.next is not None and currnode.next.data < newnode.data:
            currnode = currnode.next

        newnode.next = currnode.next
        currnode.next = newnode


if __name__ == "__main__":
    ll = LinkedList.LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(6)
    ll.add_node(7)

    newnode = LinkedList.Node(5)
    sortedInsert(ll, newnode)
    ll.list_print()

