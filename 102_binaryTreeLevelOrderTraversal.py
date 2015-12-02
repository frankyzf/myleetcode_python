__author__ = 'feng'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return []
        q = [root]
        while len(q):
            res.append(list(map(lambda n: n.val, q)))
            level = []
            for i in xrange(0, len(q)):
                if q[i].left:
                    level.append(q[i].left)
                if q[i].right:
                    level.append(q[i].right)
            q = level
        return res


if __name__ == '__main__':
    s = Solution()