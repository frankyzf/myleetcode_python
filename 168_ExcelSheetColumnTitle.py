__author__ = 'feng'

from util import *
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []

        while n > 1:
            r = (n-1)%26 + ord('A')
            c = chr(r)
            res.append(c)
            n = n//26
        reversed(res)
        return "".join(res)

if __name__ == '__main__':
    s = Solution()
    print s.convertToTitle(1)
    print s.convertToTitle(26)