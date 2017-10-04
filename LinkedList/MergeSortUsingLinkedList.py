# http://www.geeksforgeeks.org/merge-sort-for-linked-list/

# Merge Sort using LinkedList
#ToDo: RuntimeError: maximum recursion depth exceeded

import LinkedList


#split given list into two and return first element of second half
def getMiddleNode(node):
    currentnode = node
    slow, fast = currentnode, currentnode
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def sortedList(left, right):
    result = None

    if left and not right:
        result = left
    elif not left and right:
        result = right
    elif left.data < right.data:
        result = left
        result.next = sortedList(left.next, right)
    elif left.data > right.data:
        result = right
        result.next = sortedList(left, right.next)
    return result


def mergeSort(node):

    if node is None or node.next is None:
        return node

    middlenode = getMiddleNode(node)
    nexttomiddle = middlenode.next

    middlenode.next = None

    left = mergeSort(node)
    right = mergeSort(nexttomiddle)
    srtlst = sortedList(left, right)
    return srtlst




if __name__ == "__main__":
    ll = LinkedList.LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(6)
    ll.add_node(7)

    sortedlst = mergeSort(ll.cur_node)
    # ll.list_print(ll.cur_node)