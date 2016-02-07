import SampleLinkedList


def ReverseAlternateNode(head):
    count = 1
    currnode = head
    evennode = None
    prevnode = None
    while currnode:
        nextnode = None
        islast = False if currnode.next else True
        if count % 2 == 0:
            nextnode = currnode.next
            currnode.next = evennode
            evennode = currnode
            prevnode.next = nextnode
        prevnode = currnode
        currnode = nextnode if nextnode else None if islast else currnode.next
        count += 1

    newcurnode = head

    while newcurnode.next:
        newcurnode = newcurnode.next

    newcurnode.next = evennode

    return head


# trying to solve this by using stack
def ReverseAlternateNode1(head):
    evennodelst = []
    count = 1
    currnode = head
    prevnode = None
    while currnode:
        #islast = False if currnode.next else True
        if count % 2 == 0:
            #nextnode = currnode.next
            evennodelst.insert(0, currnode)
            prevnode.next = currnode.next
        prevnode = currnode
        #currnode = nextnode if nextnode else None if islast else currnode.next
        currnode = currnode.next
        count += 1
    # print "prevnode: ", prevnode.data

    newcurnode = head

    while newcurnode.next:
        newcurnode = newcurnode.next
    newcurnode.next = evennodelst[0]
    newcurnode = newcurnode.next
    newcurnode.next = evennodelst[1]


    # print "even list: ", evennodelst

    # for node in evennodelst:
    #     newcurnode.next = node
    #     newcurnode = newcurnode.next
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

    newlst = ReverseAlternateNode1(ll.cur_node)
    ll.list_print(newlst)
    # print "Odd List: "
    # ll.list_print(oddnode)
    #
    # print "\nEvent List: "
    # ll.list_print(evennode)
