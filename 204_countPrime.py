__author__ = 'feng'

from util import *
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        if n == 1:
            return 1
        ss = []
        ee = (int)(math.sqrt(n+1)) + 1
        for a in xrange(2, ee):
            badd = True
            for b in ss:
                if a%b == 0:
                    badd = False
                    break
            if badd:
                ss.append(a)

        return len(ss)


if __name__ == '__main__':
    s = Solution()
    print s.countPrimes(499979)