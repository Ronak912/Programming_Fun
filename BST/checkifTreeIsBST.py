# http://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/

# Soln 3 and 4

from DataStructures import BinarySearchTreeImplementation as bst

#ToDo: check this for correct solutions
# https://leetcode.com/submissions/detail/201508768/

if __name__ == "__main__":
    mytree = bst.BinarySearchTree()

    mytree.put(3, 'red')
    mytree.put(4, 'blue')
    mytree.put(6, 'yellow')
    mytree.put(2, 'at')


    print "Root: ", mytree.root.hasLeftChild().key

#    print "Root: ", mytree.root.leftChiLd, mytree.root.rightChiLd

    inorderlst = mytree.inOrderASlst(mytree.root)
    prev_val, curr_val = None, None
    isBST = True
    for val in inorderlst:
        if prev_val and prev_val > val:
            isBST = False
            break
        prev_val = val

    print "IS BST: ", isBST





