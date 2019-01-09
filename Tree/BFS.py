# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # BFS Traversal
        if not root:
            return []
        largevals = [root.val]
        queue = [root]
        while any(queue):
            queue = [leaf for node in queue for leaf in (node.left, node.right) if leaf]
            if queue:
                maxval = max([node.val for node in queue])
                largevals.append(maxval)
        return largevals

        """ Another way of BFS
        q = [root]
        ans = []
        while any(q):
            ans.append(max(node.val for node in q))
            newq = []
            for node in q:
                if node.left: newq.append(node.left)
                if node.right: newq.append(node.right)
            q = newq
        return ans"""

