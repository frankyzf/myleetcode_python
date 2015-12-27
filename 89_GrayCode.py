from util import *


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        res = [0, 1]
        for i in range(1, n):
            high = 2**i
            res1 = []
            for j in range(len(res)-1, -1, -1):
                res1.append(res[j] + high)
            res.extend(res1)
        return res


if __name__ == '__main__':
    s = Solution()
    print s.grayCode(2)