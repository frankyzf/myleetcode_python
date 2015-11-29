__author__ = 'feng'


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        tlen = numRows*2-2
        i =0
        res=[]
        while( i < len(s)):
            res.append(s[i])
            i += tlen

        for i in xrange(1, numRows-1):
            tlen -=2

