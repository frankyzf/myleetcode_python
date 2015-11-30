__author__ = 'feng'

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        n -= n &(-n)
        return n == 0

if __name__ == '__main__':
    s = Solution()