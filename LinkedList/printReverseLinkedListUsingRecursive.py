# http://www.geeksforgeeks.org/write-a-recursive-function-to-print-reverse-of-a-linked-list/

# Write a recursive function to print reverse of a Linked List

import LinkedList


def printReverseRecur(node):
    if node is None:
        return

    printReverseRecur(node.next)
    print node.data,


if __name__ == "__main__":
    ll = LinkedList.LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(6)
    ll.add_node(7)

    printReverseRecur(ll.cur_node)

