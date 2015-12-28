from util import *


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = ListNode(0)
        prev.next =head
        totalh = prev
        p1 = head
        p2 = None
        if p1:
            p2 = p1.next
        while p1 and p2:
            p3 = p2.next
            prev.next, p1.next, p2.next = p2, p2.next, p1
            prev, p1 = p1, p1.next
            if p1:
                p2 = p1.next
            else:
                p2 = None
        return totalh.next


if __name__ == '__main__':
    s = Solution()
    head = constructList([1,2,3])
    head = s.swapPairs(head)