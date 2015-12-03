__author__ = 'feng'

from util import *

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.num = nums
        self.rg = [0]
        if len(nums) > 0:
            s = nums[0]
            self.rg.append(s)
            for i in xrange(1, len(nums)):
                s += nums[i]
                self.rg.append(s)


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.rg[j+1] - self.rg[i]


if __name__ == '__main__':
    s = NumArray()