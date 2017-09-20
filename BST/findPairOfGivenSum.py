# http://www.geeksforgeeks.org/find-a-pair-with-given-sum-in-bst/

from DataStructures import BinarySearchTreeImplementation as bst


# This take O(N) extra space while we can only use at max log(N)
def findPair1(node, sumval):
    inorderlst = mytree.inOrderASlst(node, [])
    print inorderlst
    start, end = 0, len(inorderlst)-1
    while start < end:
        if inorderlst[start] + inorderlst[end] == sumval:
            return (inorderlst[start], inorderlst[end])
        elif inorderlst[start] + inorderlst[end] > sumval:
            end -= 1
        elif inorderlst[start] + inorderlst[end] < sumval:
            start += 1
    return None

def isPairPresent(root, target):
    # // Create two stacks. s1 is used for normal inorder traversal
    # // and s2 is used for reverse inorder traversal
    s1, s2 = [], []

    # // Note the sizes of stacks is MAX_SIZE, we can find the tree size and
    # // fix stack size as O(Logn) for balanced trees like AVL and Red Black
    # // tree. We have used MAX_SIZE to keep the code simple
    #
    # // done1, val1 and curr1 are used for normal inorder traversal using s1
    # // done2, val2 and curr2 are used for reverse inorder traversal using s2
    done1, done2 = False, False
    val1, val2 = 0, 0
    curr1, curr2 = root, root

    # // The loop will break when we either find a pair or one of the two
    # // traversals is complete
    while True:
        # // Find next node in normal Inorder traversal. See following post
        # // http://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
        while not done1:
            if curr1 is not None:
                s1.append(curr1)
                curr1 = curr1.leftChild
            else:
                if len(s1) == 0:
                    done1 = True
                else:
                    curr1 = s1.pop()
                    val1 = curr1.key
                    curr1 = curr1.rightChild
                    done1 = True


        # // Find next node in REVERSE Inorder traversal. The only
        # // difference between above and below loop is, in below loop
        # // right subtree is traversed before left subtree
        while not done2:
            if curr2 is not None:
                s2.append(curr2)
                curr2 = curr2.rightChild
            else:
                if len(s2) == 0:
                    done2 = True
                else:
                    curr2 = s2.pop()
                    val2 = curr2.key
                    curr2 = curr2.leftChild
                    done2 = True

        # If we find a pair, then print the pair and return. The first
        # condition makes sure that two same values are not added
        print val1, "==", val2
        if ((val1 != val2) and (val1 + val2) == target):
            print("\n Pair Found: %d + %d = %d\n", val1, val2, target)
            return True

        # // If sum of current values is smaller, then move to next node in
        # // normal inorder traversal
        elif (val1 + val2) < target:
            done1 = False

        # // If sum of current values is greater, then move to next node in
        # // reverse inorder traversal
        elif (val1 + val2) > target:
            done2 = False

        # // If any of the inorder traversals is over, then there is no pair
        # // so return false
        if val1 >= val2:
            return False


if __name__ == "__main__":

    mytree = bst.BinarySearchTree()
    mytree.put(20, 'red')
    mytree.put(14, 'blue')
    mytree.put(22, 'yellow')
    mytree.put(12, 'at')
    mytree.put(16, 'att')
    mytree.put(8, 'we')
    mytree.put(13, 'wew')
    mytree.put(18, 'wew')


    #print findPair1(mytree.root, 30)
    print isPairPresent(mytree.root, 26)