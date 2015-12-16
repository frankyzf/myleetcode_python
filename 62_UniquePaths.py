from util import *


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        data = [[0 for y in range(n)] for x in range(m) ]
        for i in xrange(0, m):
            data[i][0] = 1
        for j in xrange(0, n):
            data[0][j] = 1
        for i in xrange(1, m):
            for j in xrange(1, n):
                data[i][j] = data[i-1][j] + data[i][j-1]
        return data[m-1][n-1]


if __name__ == '__main__':
    s = Solution()
    