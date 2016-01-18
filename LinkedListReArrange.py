#http://www.geeksforgeeks.org/rearrange-a-given-linked-list-in-place/

# Examples:
# Input:  1 -> 2 -> 3 -> 4
# Output: 1 -> 4 -> 2 -> 3
#
# Input:  1 -> 2 -> 3 -> 4 -> 5
# Output: 1 -> 5 -> 2 -> 4 -> 3

# 1) Find the middle point using tortoise and hare method.
# 2) Split the linked list in two halves using found middle point in step 1.
# 3) Reverse the second half.
# 4) Do alternate merge of first and second halves.


import SampleLinkedList

# Having issues with this function, does not work as expected
def mergeLinkedList(first, second):
    if not first and not second:
        return None

    if not second:
        return first

    if not first:
        return second

    # newlst = first
    # newlst.next = second
    # return newlst
    # currfirst, currsecond = first.next, second.next

    tmpnode = SampleLinkedList.Node(0)

    newlst = tmpnode
    currfirst, currsecond = first, second
    while currfirst and currsecond:
        print "inside loop: ", currfirst.data, currsecond.data
        # newlst.next = currfirst
        # newlst = newlst.next
        #
        # newlst.next = currsecond
        # newlst = newlst.next

        currfirst = currfirst.next
        currsecond = currsecond.next


    # while currfirst:
    #     newlst.next = currfirst
    #     currfirst = currfirst.next
    #
    # while currsecond:
    #     newlst.next = currsecond
    #     currsecond = currsecond.next
    newlst = tmpnode.next
    return newlst


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

    first = ll.cur_node
    second = ll.split()

    #print "First element of second list: ", second.data
    ll.list_print(first)

    revsecond = ll.reverseLinkList(second)

    print "\nSecond reverse linkedlist: "
    ll.list_print(revsecond)

    print "\n\n"

    resultlist = mergeLinkedList(first, revsecond)
    print "here"
    ll.list_print(resultlist)