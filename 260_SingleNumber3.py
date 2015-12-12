__author__ = 'feng'

from util import *
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        v = nums[0]
        for i in xrange(1, len(nums)):
             v ^= nums[i]
        flag = 1
        while flag & v == 0:
            flag <<= 1
        res = [0,0]
        for i in xrange(0, len(nums)):
            if flag & nums[i]:
                res[0] ^= nums[i]
            else:
                res[1] ^= nums[i]
        return res



if __name__ == '__main__':
    s = Solution()