__author__ = 'feng'

from util import *
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        prime = [True] * max(n, 2)
        prime[0], prime[1] = False, False
        base = 2
        while base*base < n:
            if prime[base]:
                i = 2
                while i * base < n:
                    prime[i*base] = False
                    i += 1
            base += 1
        return sum(prime)


if __name__ == '__main__':
    s = Solution()
    print s.countPrimes(499979)