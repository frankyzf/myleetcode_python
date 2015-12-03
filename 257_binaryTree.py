__author__ = 'feng'

from util import *
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        p = [str(root.val)]
        if not(root.left or root.right):
            res.append(p)
        if root.left:
            self.btp(root.left, p[:], res)
        if root.right:
            self.btp(root.right, p, res)

        return list(map(lambda x: "->".join(x), res))

    def btp(self, root, ll, res):
        ll.append(str(root.val))
        if not( root.left or root.right):
            res.append(ll)
        if root.left:
            self.btp(root.left, ll[:] res)
        if root.right:
            self.btp(root.right, ll, res)




if __name__ == '__main__':
    s = Solution()
    root = constructTree("1,2")
    a = s.binaryTreePaths(root)
    print a