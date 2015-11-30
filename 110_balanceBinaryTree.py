__author__ = 'feng'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        a, b = self.depth(root)
        return b

    def depth(self, root):
        if not root:
            return 0, True
        ln, lb = self.depth(root.left)
        rn, rb = self.depth(root.right)
        b = lb and rb and abs(ln -rn) <= 1
        return max(ln, rn)+1, b


if __name__ == '__main__':
    s = Solution()