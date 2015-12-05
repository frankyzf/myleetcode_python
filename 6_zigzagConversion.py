__author__ = 'feng'

from util import *
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0:
            return ""
        if numRows == 1:
            return s

        head = []
        tail = []
        body = []
        for i in xrange(0, len(s), 2*numRows-2):
            head.append(s[i])
        for i in xrange(1, numRows-1):
            for j in xrange(i, len(s), 2*numRows-2 ):
                body.append(s[j])
                if j+2*numRows-2*i -2 < len(s):
                    body.append(s[j+2*numRows-2*i -2])
        for i in xrange(numRows-1, len(s), 2*numRows-2):
            tail.append(s[i])
        return "".join(head) + "".join(body) + "".join(tail)



if __name__ == '__main__':
    s = Solution()
    print s.convert("PAYPALISHIRING", 3)