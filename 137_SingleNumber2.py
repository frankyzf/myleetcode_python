from util import *


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [0]*32
        for n in nums:
            m = 1
            for i in xrange(0, 32):
                if n & m:
                    bits[i] += 1
                    if bits[i] >= 3:
                        bits[i] -= 3
                m <<= 1
        t = 0
        m = 1
        neg = False
        if not bits[31] == 0:
            neg = True
            bits[31] = 0
            for i in xrange(0, 31):
                if bits[i] == 0:
                    bits[i] = 1
                else:
                    bits[i] = 0

        for i in xrange(0, 32):
            if bits[i]:
                t |= m
            m <<= 1
        if neg:
            t += 1
            t *= -1
        return t

if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([2,2,3,2])