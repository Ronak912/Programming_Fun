#http://www.geeksforgeeks.org/convert-bst-to-a-binary-tree/

from DataStructures import BinarySearchTreeImplementation as bst


def printInOrder(root):
    if not root:
        return
    printInOrder(root.leftChild)
    print root.key,
    printInOrder(root.rightChild)

def printPreOrder(root):
    if not root:
        return
    print root.key,
    printInOrder(root.leftChild)
    printInOrder(root.rightChild)

def addGreaterKeysUtil(root, sum):
    if not root:
        return
    addGreaterKeysUtil(root.rightChild, sum)
    sum += root.key
    print root.key, "===", sum
    root.key = sum
    addGreaterKeysUtil(root.leftChild, sum)



def addGreaterKeys(root):
    newroot = addGreaterKeysUtil(root, 0)
    return newroot


if __name__ == "__main__":

  #       20
  #   14           22
  # 12    16
  #8   13  15   18
    mytree = bst.BinarySearchTree()
    mytree.put(20, 'red')
    mytree.put(14, 'blue')
    mytree.put(22, 'yellow')
    mytree.put(12, 'at')
    mytree.put(16, 'att')
    mytree.put(8, 'we')
    mytree.put(13, 'wew')
    mytree.put(15, 'wew')
    mytree.put(18, 'wew')

    # printInOrder(mytree.root)
    printPreOrder(mytree.root)
    addGreaterKeys(mytree.root)
    print
    print "========"
    printInOrder(mytree.root)

