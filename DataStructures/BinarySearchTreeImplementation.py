# handle duplicate entries in BST: http://www.geeksforgeeks.org/how-to-handle-duplicates-in-binary-search-tree/
# Difference between BST and Hash Table: http://www.geeksforgeeks.org/advantages-of-bst-over-hash-table/

# Find smallest K nodes in BST:
# http://www.geeksforgeeks.org/find-k-th-smallest-element-in-bst-order-statistics-in-bst/

# To get nodes in desc order, use reverse In-Order traversal: RNL
# To get kth largest element: http://www.geeksforgeeks.org/kth-largest-element-in-bst-when-modification-to-bst-is-not-allowed/

# count number of sub-trees in given range:
# http://www.geeksforgeeks.org/count-bst-subtrees-that-lie-in-given-range/

# check if given tree is BST or not
# http://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/

class TreeNode:

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    # This is iterative solution
    def insert(self, key, val):
        if not self.root:
            self.root = TreeNode(key, val)
            return
        current = self.root
        while True:
            parent = current
            if key < current.key:
                current = current.leftChild
                if not current:
                    parent.leftChild = TreeNode(key, val, parent=parent)
                    return
            else:
                current = current.rightChild
                if not current:
                    parent.rightChild = TreeNode(key, val, parent=parent)
                    return

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            return None
        return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
        self.delete(key)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def remove(self, currentNode):
        if currentNode.isLeaf(): #leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): #interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else:   # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    # Root node with only left children
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    # root node with only right children
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)

    def __iter__(self):
        print "inside"
        if self:
            if self.hasLeftChild():
                for elem in self.leftChiLd:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def getMaxDepth(self, node):
        if not node:
            return 0

        print "Node: ", node
        print "key: ", node.key
        print "Value: ", node.payload

        left = self.getMaxDepth(node.leftChiLd)
        right = self.getMaxDepth(node.rightChild)

        return 1 + max(left, right)

    # This is asc sort traversal
    # LNR (Left, Node, Right)
    def inOrder(self, node):
        if node:
            self.inOrder(node.leftChild)
            print "{}:{}".format(node.key, node.payload)
            self.inOrder(node.rightChild)

    def inOrderASlst(self, node, tmplst):
        if node:
            self.inOrderASlst(node.leftChild, tmplst)
            tmplst.append(node.key)
            self.inOrderASlst(node.rightChild, tmplst)
        return tmplst

    # This is DFS traversal
    # NLR
    def preOrder(self, node):
        if node:
            print "{}:{}".format(node.key, node.payload)
            self.preOrder(self, node.leftChild)
            self.preOrder(self, node.rightChild)

    #LRN
    def postOrder(self, node):
        if node:
            self.postOrder(self, node.leftChild)
            self.postOrder(self, node.rightChild)
            print "{}:{}".format(node.key, node.payload)


    # Print nodes at a given level
    def printGivenLevel(self, root, level):
        if root is None:
            return
        if level == 1:
            print "%d" %(root.data),
        elif level > 1:
            self.printGivenLevel(root.left, level-1)
            self.printGivenLevel(root.right, level-1)

    # http://www.cs.duke.edu/courses/spring00/cps100/assign/trees/diameter.html
    def diameter(self, node):
        if not node:
            return 0

        lheight = self.getMaxDepth(node.leftChiLd)
        rheight = self.getMaxDepth(node.rightChild)

        ldiameter = self.diameter(node.leftChiLd)
        rdiameter = self.diameter(node.rightChild)

        return max(lheight + rheight + 1, max(ldiameter, rdiameter))


if __name__ == '__main__':

    mytree = BinarySearchTree()

    mytree[3] = "red"
    mytree[4] = "blue"
    mytree[6] = "yellow"
    mytree[2] = "at"

    print(mytree[6])
    print(mytree[2])

    print "Root: ", mytree.root

#    print "Root: ", mytree.root.leftChiLd, mytree.root.rightChiLd

    mytree.inOrder(mytree.root)

    #print mytree.getMaxDepth(mytree.root)
    # for node in mytree:
    #     print node
