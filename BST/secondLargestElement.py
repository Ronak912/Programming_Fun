# http://www.geeksforgeeks.org/second-largest-element-in-binary-search-tree-bst/

from DataStructures import BinarySearchTreeImplementation as bst

secondlargest = None
count = 0

def getSecondLargestElement(node):
    '''The second largest element is second last element in inorder traversal and second element in reverse inorder traversal.
    We traverse given Binary Search Tree in reverse inorder and keep track of counts of nodes visited.
    Once the count becomes 2, we print the node.'''
    global secondlargest, count
    if node is None or count > 2:
        return None

    getSecondLargestElement(node.rightChild)
    count += 1
    if count == 2:
        secondlargest = node.key
        return
    getSecondLargestElement(node.leftChild)



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


    getSecondLargestElement(mytree.root)
    print "Second Largest: ", secondlargest