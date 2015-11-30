__name__ = 'feng'
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while(n):
            n -= n & (-n)
            cnt += 1
        return cnt

if __name__ == '__main__':
    s = Solution()