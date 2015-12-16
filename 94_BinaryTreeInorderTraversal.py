from util import *


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        st = []
        p = root
        while p:
            st.append(p)
            p = p.left
        while len(st):
            p = st.pop()
            res.append(p.val)
            p = p.right
            while p:
                st.append(p)
                p = p.left

        return res


if __name__ == '__main__':
    s = Solution()
    