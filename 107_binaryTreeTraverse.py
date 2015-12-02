__author__ = 'feng'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        a = [root]
        r=[]
        while len(a):
            r.append(list(map(lambda x: x.val, a)))
            b = []
            for i in xrange(0, len(a)):
                if a[i].left:
                    b.append(a[i].left)
                if a[i].right:
                    b.append(a[i].right)
            a = b
        r.reverse()
        return r






if __name__ == '__main__':
    s = Solution()
    import util
    root = util.constructTree("3,9,20,#,#,15,7")
    s.levelOrderBottom(root)