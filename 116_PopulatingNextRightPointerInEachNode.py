from util import *



class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        st = []
        if root:
            st.append(root)
        while len(st):
            st1 = []
            while len(st):
                p = st.pop(0)
                if len(st) > 0:
                    p.next = st[0]
                if p.left:
                    st1.append(p.left)
                if p.right:
                    st1.append(p.right)
            st = st1


if __name__ == '__main__':
    s = Solution()
    