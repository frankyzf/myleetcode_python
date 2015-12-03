__author__ = 'feng'

from util import *
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        for i in xrange(0, len(haystack)-len(needle)+1):
            j = 0
            while j < len(needle):
                if haystack[i+j] != needle[j]:
                    break;
                j += 1
            if j == len(needle):
                return i
        return -1


if __name__ == '__main__':
    s = Solution()