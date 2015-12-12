__author__ = 'feng'

from util import *

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v = nums[0]
        for i in xrange(1, len(nums)):
            v ^= nums[i]
        return v


if __name__ == '__main__':
    s = Solution()