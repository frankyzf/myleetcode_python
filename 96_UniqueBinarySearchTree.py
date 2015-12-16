from util import *


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = [0]*(n+1)
        cnt[0] =1
        cnt[1] = 1
        for m in xrange(2, n+1):
            for l in xrange(0, m):
                cnt[m] += cnt[l]*cnt[m-1-l]
        return cnt[n]


if __name__ == '__main__':
    s = Solution()
    