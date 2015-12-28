from util import *


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import copy
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        res = []
        r = [grid[0][0]]
        for i in range(1, len(grid[0])):
            r.append(r[-1] + grid[0][i])
        res.append(copy.copy(r))
        for j in range(1, len(grid)):
            r = [res[j-1][0]+grid[j][0]]
            for i in range(1, len(grid[0])):
                p = min(res[j-1][i], r[i-1]) + grid[j][i]
                r.append(p)
            res.append(copy.copy(r))
        return res[len(grid)-1][len(grid[0])-1]



if __name__ == '__main__':
    s = Solution()
    