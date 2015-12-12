__author__ = 'feng'

from util import *
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        i = 1
        while i < len(prices) and prices[i] < prices[i-1]:
            i += 1
        begin = i -1
        v = 0
        while i < len(prices):
            begin = i -1
            while i < len(prices) and prices[i] >= prices[i-1]:
                i += 1
            v += prices[i-1] - prices[begin]
            while i < len(prices) and prices[i] < prices[i-1]:
                i += 1
        return v


if __name__ == '__main__':
    s = Solution()