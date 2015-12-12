__author__ = 'feng'

from util import *

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        h = nums[0:k]
        reversed(h)
        t = []
        if k < len(nums):
            t = nums[k:]
            reversed(t)
        t.extend(h)
        nums = t

if __name__ == '__main__':
    s = Solution()
    s.rotate([1, 2], 1)