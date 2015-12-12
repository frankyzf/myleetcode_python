__author__ = 'feng'

from util import *
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = list(filter(lambda x: not x == 0, nums))
        if len(n) == 0:
            return [0] * len(nums)
        v = reduce(lambda x, y: x * y, n)
        if len(nums) - len(n) == 0:
            return list(map(lambda x: v/x, nums))
        elif len(nums) - len(n) == 1:
            j = nums.index(0)
            a = [0]*j
            a.append(v)
            a.extend([0]*(len(nums)-j-1))
            return a
        else:
            return [0] * len(nums)



if __name__ == '__main__':
    s = Solution()
    print s.productExceptSelf([0,0])