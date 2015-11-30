__name__ = 'feng'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        prev, p = head, head.next
        while  p:
            if prev.val == p.val:
                prev.next = p.next
                p = p.next
            else:
                prev, p = p, p.next
        return head

if __name__ == '__main__':
    s = Solution()