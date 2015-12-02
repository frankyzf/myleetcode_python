__author__ = 'feng'

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = 0
        p = head
        while p:
            l += 1
            p = p.next
        l -= n
        l -= 1
        while l > 0:
            head = head.next
            l -= 1
        return head



if __name__ == '__main__':
    s = Solution()