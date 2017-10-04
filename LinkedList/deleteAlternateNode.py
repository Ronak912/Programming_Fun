# http://www.geeksforgeeks.org/delete-alternate-nodes-of-a-linked-list/

# Delete alternate nodes of a Linked List

import LinkedList


def deleteAlternateNode(node):
    prev = node
    if node.next is None:
        return
    currnode = node.next
    while prev and currnode:
        prev.next = currnode.next
        currnode = None
        prev = prev.next
        if prev is not None:
            currnode = prev.next



if __name__ == "__main__":
    ll = LinkedList.LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(6)
    ll.add_node(7)

    deleteAlternateNode(ll.cur_node)
    ll.list_print(ll.cur_node)