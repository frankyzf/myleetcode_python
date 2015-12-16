from util import *




class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        m = nums[0]
        a = nums[0]
        for i in xrange(1, len(nums)):
            if a < 0:
                a = nums[i]
            else:
                a += nums[i]
            if a > m:
                m = a
        return m




if __name__ == '__main__':
    s = Solution()
    print s.maxSubArray([-2,1,-3,4,-1,2,1, -5, 4])