__author__ = 'feng'

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from util import ListNode

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        phead = ListNode(0)
        phead.next = head
        p = phead
        while p:
            while p.next and p.next.val == val:
                p.next = p.next.next
            p = p.next
        return phead.next


if __name__ == '__main__':
    s = Solution()