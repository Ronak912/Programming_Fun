# http://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/

# Check if tree is Binary tree or not


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __int__(self):
        self.root = None

    def isBSTUtil(self, node, min, max):
        if node:
            print "data: ", node.data, "==", min, "==", max
        if not node:
            return True
        elif node.data < min or node.data > max:
            return False
        else:
            return (self.isBSTUtil(node.left, min, node.data-1) and self.isBSTUtil(node.right, node.data+1, max))


    def isBST(self):
        return self.isBSTUtil(self.root, 0, 15)


if __name__ == "__main__":
    bst = BinaryTree()
    bst.root = Node(4)
    bst.root.left = Node(2)
    bst.root.right = Node(10)
    bst.root.left.left = Node(1)
    bst.root.left.right = Node(3)
    #bst.root.left.left.left = Node(10)
    bst.root.right.right = Node(11)
    print bst.isBST()