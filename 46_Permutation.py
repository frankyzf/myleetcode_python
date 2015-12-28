from util import *


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        nums.sort()
        res = [nums]
        import math
        import copy
        for i in xrange(math.factorial(len(nums))-1):
            a = res[-1]
            j = len(nums) -2
            while j >= 0 and a[j] > a[j+1]:
                j -= 1
            t1 = a[j]
            k1 = j
            while j < len(nums) and a[j] >= t1:
                j += 1
            k2 = j-1
            t2 = a[k2]
            a = res[-1][:k1]
            b = res[-1][k1+1:]
            b[k2-k1-1] = t1
            a.append(t2)
            a.extend(sorted(b))
            res.append(a)

        return res



if __name__ == '__main__':
    s = Solution()
    print s.permute([1,2,3])