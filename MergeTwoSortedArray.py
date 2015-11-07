__author__ = 'feng'


# Definition for singly-linked list.
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
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next
        if l1:
            l.next = l1
        else:
            l.next = l2

        return head.next

if __name__ == '__main__':
     l1 = ListNode(2)
     l2 = ListNode(1)
     l = Solution().mergeTwoLists(l1, l2)
     print l