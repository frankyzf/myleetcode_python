__author__ = 'feng'
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from util import *

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        if n < 2:
            return True
        pn = n//2

        t1 = head
        for i in xrange(0, pn-1):
            t1 = t1.next
        t2 = t1.next
        t1.next = None

        p1 = None
        p2 = t2
        while p2:
            p3 = p2.next
            p2.next = p1
            p1,p2 = p2, p3
        h2 = p1
        h1 = head
        b = True
        for i in xrange(0, pn):
            if h1.val != h2.val:
                b = False
                break
            h1, h2 = h1.next, h2.next
        h2 = p1
        p1 = None
        p2 = h2
        while p2:
            p3 = p2.next
            p2.next = p1
            p1, p2 = p2, p3
        t1.next = p1
        return b

if __name__ == '__main__':
    s = Solution()
    root = constructList([1,2])
    print s.isPalindrome(root)