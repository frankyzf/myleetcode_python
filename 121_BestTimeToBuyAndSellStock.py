from util import *


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        bpoint = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            p = prices[i]
            if p < bpoint:
                bpoint = p
            elif p - bpoint > profit:
                profit = p - bpoint
        return profit

if __name__ == '__main__':
    s = Solution()
    