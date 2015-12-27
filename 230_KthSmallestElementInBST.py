from util import TreeNode


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        st = []
        p = root
        lastnode = root
        while p:
            st.append(p)
            p = p.left
        while k > 0 and len(st) > 0:
            p = st.pop()
            k -= 1
            lastnode = p
            if p.right:
                p = p.right
                while p:
                    st.append(p)
                    p = p.left
        return lastnode.val


if __name__ == '__main__':
    s = Solution()
    