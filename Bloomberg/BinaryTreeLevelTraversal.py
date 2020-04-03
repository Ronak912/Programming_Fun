# Recursive Python program for level order traversal of Binary Tree

# A node structure
class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Function to  print level order traversal of tree
def printLevelOrder(root):
    #method-1
    # h = height(root)
    # for i in range(1, h+1):
    #     printGivenLevel(root, i)
    queue = [root]
    while queue:
        vals = [node.data for node in queue]
        for val in vals:
            print val,
        #method-2
        # newq = []
        # for node in queue:
        #     if node.left:
        #         newq.append(node.left)
        #     if node.right:
        #         newq.append(node.right)
        # queue = newq
        #method-3, list comprehension
        queue = [leaf for node in queue for leaf in (node.left, node.right) if leaf]


# Print nodes at a given level
def printGivenLevel(root , level):
    if root is None:
        return
    if level == 1:
        print "%d" %(root.data),
    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)


""" Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
"""
def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        #Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1
        # return 1 + max(lheight, rheight)


count = 0
# Number of subtree that lies within given range
# http://www.geeksforgeeks.org/count-bst-subtrees-that-lie-in-given-range/
def countSubTrees(node, low, high):
    global count

    if node is None:
        return True

    islefttreeinrange = True
    if node.left:
        islefttreeinrange = countSubTrees(node.left, low, high)

    isrighttreeinrange = True
    if node.right:
        isrighttreeinrange = countSubTrees(node.right, low, high)


    if node.data >= low and node.data <= high and islefttreeinrange and isrighttreeinrange:
        count += 1
        return True
    return False


def getCount(node, low, high):
    # Base case
    if not node:
        return 0

    # Special Optional case for improving efficiency
    if node.data == low and node.data == high:
        return 1

    # If current node is in range, then include it in count and
    # recur for left and right children of it
    if node.data >= low and node.data <= high:
        return 1 + getCount(node.left, low, high) + getCount(node.right, low, high)

    # If current node is smaller than low, then recur for right
    # child
    elif node.data <= low:
        return getCount(node.right, low, high)

    # Else recur for left child
    else:
        return getCount(node.left, low, high)



# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print "Level order traversal of binary tree is -"
printLevelOrder(root)

# bstroot = Node(10)
# bstroot.left = Node(5)
# bstroot.right = Node(50)
# bstroot.left.left = Node(1)
# bstroot.right.left = Node(40)
# bstroot.right.right = Node(100)
#
# countSubTrees(bstroot, 1, 45)
# print "Count: ", count
#
# # http://www.geeksforgeeks.org/count-bst-nodes-that-are-in-a-given-range/
# print "Total Nodes: ", getCount(bstroot, 5, 45)