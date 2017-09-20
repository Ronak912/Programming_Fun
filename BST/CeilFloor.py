# http://www.geeksforgeeks.org/floor-and-ceil-from-a-bst/

from DataStructures import BinarySearchTreeImplementation as bst

#ToDo: below solution is not working as expected


# Function to find ceil of a given input in BST. If input
# is more than the max key in BST, return -1
def ceil(root, inp):
    if root is None:
        return None

    if root.key == inp:
        return root.key

    if root.key < inp:
        ceil(root.rightChild, inp)

    ceilval = ceil(root.leftChild, inp)
    return ceilval if ceilval >= inp else root.key





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

    print ceil(mytree.root, 12)
    print ceil(mytree.root, 14)
    print ceil(mytree.root, 16)