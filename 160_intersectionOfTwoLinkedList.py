__author__ = 'feng'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = []
        while headA:
            a.append(headA)
            headA = headA.next
        b = set(a)
        while headB:
            if headB in b:
                return headB
            headB = headB.next
        return None


if __name__ == '__main__':
    s = Solution()