__author__ = 'feng'

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode(0)
        head = l
        while l1 and l2:
            if l1.val < l2.val:
                l1, l.next = l1.next, l1
                l = l.next
            else:
                l2, l.next = l2.next, l2
                l = l.next
        if l1:
            l.next = l1
        if l2:
            l.next = l2
        return head.next

if __name__ == '__main__':
    s = Solution()
    l1  = ListNode(1)
    l2 = ListNode(2)
    r = s.mergeTwoLists(l1, l2)