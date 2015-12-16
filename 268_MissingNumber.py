from util import *


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = list(map(lambda x: False, xrange(0, len(nums)+1)))
        for n in nums:
            flag[n] = True
        for i in xrange(0, len(nums)+1):
            if not flag[i]:
                return i

if __name__ == '__main__':
    s = Solution()
    