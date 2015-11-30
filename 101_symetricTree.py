__author__ = 'feng'

# class TreeNode(object):
def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.symtwo(root.left, root.right)

    def symtwo(self, left, right):
        """
        :param left: TreeNode
        :param right: TreeNoe
        :return: bool
        """
        if not left:
            return right == None
        if not right:
            return False
        if left.val == right.val and self.symtwo(left.right, right.left)  \
                and self.symtwo(left.left, right.right):
            return True
        return False


if __name__ == '__main__':
    s = Solution()