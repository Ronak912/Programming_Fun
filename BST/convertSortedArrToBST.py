# http://www.geeksforgeeks.org/sorted-array-to-balanced-bst/

from DataStructures import BinarySearchTreeImplementation as bst


def sortedArrToBST(arr, start, end):

    if start > end:
        return

    mid = (start+end) / 2
    node = bst.TreeNode(arr[mid], 'noval')
    node.leftChild = sortedArrToBST(arr, start, mid-1)
    node.rightChild = sortedArrToBST(arr, mid+1, end)
    return node


if __name__ == "__main__":
    treeobj = bst.BinarySearchTree()

    treeobj.root = sortedArrToBST([4, 8, 10, 12, 14, 20, 22], 0, 6)
    print treeobj.root.key
    print treeobj.root.leftChild.key
    print treeobj.root.leftChild.leftChild.key
    print treeobj.root.leftChild.rightChild.key
    print treeobj.root.rightChild.key
    print treeobj.root.rightChild.leftChild.key
    print treeobj.root.rightChild.rightChild.key

    # treeobj.preOrder(treeobj.root)