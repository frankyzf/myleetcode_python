from util import *

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        profit = [0]
        for i in range(1, len(prices)):
            profit.append(prices[i]-prices[i-1])
        res = [0]
        maxp = 0
        maxprevp = 0
        for i in range(1, len(prices)):
            if i > 3:
                maxprevp = max(maxprevp, res[i-3])

            res.append(profit[i] + max(res[i-1], max(maxprevp, 0)))
            maxp = max(maxp, res[-1])
        return maxp




if __name__ == '__main__':
    s = Solution()
    print s.maxProfit([1,2,3,0,2])