__author__ = 'feng'

from util import *

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if len(nums) == 0:
            return []

        i = 0
        while i < len(nums):
            before = i
            i += 1
            while i < len(nums) and nums[i] == nums[i-1] +1:
                i += 1
            if i == before + 1:
                res.append(str(nums[before]))
            else:
                res.append(str(nums[before]) + "->" + str(nums[i-1]))


        return res




if __name__ == '__main__':
    s = Solution()