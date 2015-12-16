from util import *


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()
        p = head
        while p and p not in s:
            s.add(p)
            p = p.next
        if not p:
            return False
        return True



if __name__ == '__main__':
    s = Solution()
    