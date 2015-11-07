__author__ = 'feng'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = tail = ListNode(0)
        while(l1 and l2):
            tail.next =  ListNode((l1.val + l2.val + carry)%10)
            tail = tail.next
            carry = (l1.val + l2.val + carry) / 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            tail.next = ListNode((l1.val + carry)%10)
            tail = tail.next
            carry = (l1.val + carry)/10
            l1 = l1.next
        while l2:
            tail.next = ListNode((l2.val + carry)%10)
            tail = tail.next
            carry = (l2.val + carry)/10
            l2 = l2.next
        if carry:
            tail.next = ListNode(carry)

        return head.next