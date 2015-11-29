__name__ = 'feng'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        newRoot = TreeNode(root.val)
        newRoot.left = self.invertTree(root.right)
        newRoot.right = self.invertTree(root.left)
        return newRoot


if __name__ == '__main__':
    s = Solution()