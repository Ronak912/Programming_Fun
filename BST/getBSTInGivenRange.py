# http://www.geeksforgeeks.org/print-bst-keys-in-the-given-range/

# print all the nodes that has key between k1 and k2 inclusive

from DataStructures import BinarySearchTreeImplementation as bst


def printBSTinRange(node, k1, k2):

    if not node:
        return

    if k1 < node.key:
        printBSTinRange(node.leftChild, k1, k2)

    if node.key >= k1 and node.key <= k2:
        print node.key

    if k2 > node.key:
        printBSTinRange(node.rightChild, k1, k2)


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

    printBSTinRange(mytree.root, 8, 14)