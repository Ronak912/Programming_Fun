class Node:
    def __init__(self, data):
        self.data = data  # contains the data
        self.next = None  # contains the reference to the next node


class LinkedList:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = Node(data)  # create a new node

        curnode = self.cur_node
        temp = self.cur_node

        if not curnode:
            self.cur_node = new_node
            return
        while curnode.next:
            curnode = curnode.next
        curnode.next = new_node
        self.cur_node = temp

    def delete(self, data):

        currentnode = self.cur_node
        prevnode = None
        isfound = False
        while currentnode and not isfound:
            if currentnode.data == data:
                isfound = True
                break
            prevnode = currentnode
            currentnode = currentnode.next

        if not isfound:
            print "Could not find element in list"
            return

        if not prevnode:
            self.cur_node = currentnode.next
            return

        prevnode.next = currentnode.next

    def search(self, data):

        current = self.cur_node
        while current:
            if current.data == data:
                print "Found element in list"
                return True
            current = current.next
        print "Not in List"
        return False

        # new_node.next = self.cur_node # link the new node to the 'previous' node.
        # self.cur_node = new_node #  set the current node to the new one.

    def list_print(self, head=None):
        node = head if head else self.cur_node  # cant point to ll!
        while node:
            print node.data,
            node = node.next

    def size(self):
        count = 0
        current = self.cur_node
        while current:
            count += 1
            current = current.next
        print "Total Size: ", count

    #split given list into two and return first element of second half
    def getMiddleElement(self):
        currentnode = self.cur_node
        print "Current Node: ", currentnode
        slow, fast = currentnode, currentnode
        print "Fast: ", fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print "Middle Element: ", slow.data

    def reverseLinkList(self, head=None):
        prevnode = None
        currentnode = head if head else self.cur_node
        while currentnode:
            temp = currentnode.next
            currentnode.next = prevnode
            prevnode = currentnode
            currentnode = temp
        return prevnode

    #split given list into two and return first element of second half
    def split(self):
        totallen = 1
        currentnode = self.cur_node
        slow, fast = currentnode, currentnode
        prev = None
        while fast and fast.next:
            if fast.next and fast.next.next:
                totallen += 2
            elif fast.next:
                totallen += 1
            prev = slow
            slow = slow.next
            fast = fast.next.next

        print "Total Length: ", totallen
        # delink last element of first half and return first element of second half

        # if even number of element
        if totallen % 2 == 0:
            prev.next = None
            return slow
        # odd number of element
        temp = slow.next
        slow.next = None
        return temp



if __name__ == '__main__':
    ll = LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(4)
    ll.add_node(5)

    ll.list_print()
    ll.size()

    ll.getMiddleElement()

    revhead = ll.reverseLinkList()

    ll.list_print(revhead)
