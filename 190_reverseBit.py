__author__ = 'feng'

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        h = 1 << 31
        l = 1
        v = 0
        for i in xrange(0, 32):
            if n & l != 0 :
                v |= h
            h >>= 1
            l <<= 1
        return v

if __name__ == '__main__':
    s = Solution()
    s.reverseBits(65536)