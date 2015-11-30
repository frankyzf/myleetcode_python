__name__ = 'feng'

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        else:
            a = 1
            b = 2
            c = b
            for i in xrange(3, n+1):
                c = a + b
                a, b = b, c
            return c

if __name__ == '__main__':
    s = Solution()