__author__ = 'Ronak'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N == 1:
            return [TreeNode(0)]

        nodes = []
        for i in range(1, N-1,2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(N-1-i):
                    root = TreeNode(0)
                    root.left, root.right = left, right
                    nodes.append(root)
        return nodes


if __name__ == "__main__":
    obj = Solution()
    print(obj.allPossibleFBT(7))

