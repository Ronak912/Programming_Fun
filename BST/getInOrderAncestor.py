# http://www.geeksforgeeks.org/inorder-successor-in-binary-search-tree/

# Inorder Successor in Binary Search Tree

from DataStructures import BinarySearchTreeImplementation as bst


def inOrderSuccessor(n):

    # Step 1 of the above algorithm
    if n.rightChild is not None:
        return n.rightChild.findMin().key

    # Step 2 of the above algorithm
    p = n.parent
    while (p is not None):
        # below condition is to make sure node is not right of parent otherwise parent is smaller than child
        if n.key != p.rightChild.key:
            break
        n = p
        p = p.parent

    return p


if __name__ == "__main__":
    mytree = bst.BinarySearchTree()

    mytree.put(20, 'red')
    mytree.put(8, 'blue')
    mytree.put(22, 'yellow')
    mytree.put(4, 'at')
    mytree.put(12, 'att')
    mytree.put(10, 'we')
    mytree.put(14, 'wew')

    #         20
    #     8        22
    # 4      12
    #     10    14
    # assign 10 to temp
    temp = mytree.root.leftChild.rightChild.leftChild
    succ = inOrderSuccessor(temp)
    if succ:
        print succ.key
    else:
        print "No successor"

    temp = mytree.root.rightChild
    succ = inOrderSuccessor(temp)
    if succ:
        print succ.key
    else:
        print "No successor"
