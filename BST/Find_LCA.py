#LCA: Lowest Common Ancestors

# http://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
# Complexity: O(h)


from DataStructures import BinarySearchTreeImplementation as bst

# no extra space needed
def findLCAIter(root, n1, n2):

    while root:
        if root.key > n1 and root.key > n2:
            root = root.leftChild
        elif root.key < n1 and root.key < n2:
            root = root.rightChild
        else:
            break

    return root.key

# because of recursion O(h) extra space is needed
def findLCARecur(root, n1, n2):
    if not root:
        return None
    if root.key > n1 and root.key > n2:
        return findLCARecur(root.leftChild, n1, n2)
    elif root.key < n1 and root.key < n2:
        return findLCARecur(root.rightChild, n1, n2)

    return root.key

if __name__ == "__main__":
    mytree = bst.BinarySearchTree()

    mytree.put(20, 'red')
    mytree.put(8, 'blue')
    mytree.put(22, 'yellow')
    mytree.put(4, 'at')
    mytree.put(12, 'att')
    mytree.put(10, 'we')
    mytree.put(14, 'wew')

    print "====Using Iter====="
    print findLCAIter(mytree.root, 10, 14)
    print findLCAIter(mytree.root, 8, 14)
    print findLCAIter(mytree.root, 10, 22)

    print "======Using Recurrrr====="

    print findLCARecur(mytree.root, 10, 14)
    print findLCARecur(mytree.root, 8, 14)
    print findLCARecur(mytree.root, 10, 22)