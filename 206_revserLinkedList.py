__name__ = 'feng'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            t = head.next
            head.next = prev
            prev, head = head, t
        return prev

if __name__ == '__main__':
    s = Solution()