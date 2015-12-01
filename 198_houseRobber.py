__author__ = 'feng'
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        a = 0
        b = nums[0]
        for j in xrange(1, len(nums)):
            c = max(a+nums[j], b)
            a, b = b, c
        return max(a, b)

if __name__ == '__main__':
    s = Solution()