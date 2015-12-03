__author__ = 'feng'

from util import *
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        digits = []
        for i in xrange(-1, -len(s), -1):
            digits.append(s[i])
        if s[0] == '-':
            aa = -int("".join(digits))
            if aa < -2147483648:
                aa =0
        else:
            digits.append(s[0])
            aa =  int("".join(digits))
            if aa > 2147483647:
                aa = 0
        return aa

if __name__ == '__main__':
    s = Solution()
    print s.reverse(-123)
    print s.reverse(123)