__author__ = 'feng'

from util import *
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        if len(v1) < len(v2):
            for i in xrange(len(v1), len(v2)):
                v1.append("0")
        elif len(v1) > len(v2):
            for i in xrange(len(v2), len(v1)):
                v2.append("0")
        for i in xrange(len(v1)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        return 0


if __name__ == '__main__':
    s = Solution()