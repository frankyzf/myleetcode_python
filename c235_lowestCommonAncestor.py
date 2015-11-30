__name__ = 'feng'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            (p,q) = (q,p)
        while not (root and root.val >= p.val and root.val <= q.val):
            if root.val < p.val:
                root = root.right
            else:
                root = root.left
        return root


if __name__ == '__main__':
    s = Solution()