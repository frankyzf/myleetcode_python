__author__ = 'feng'

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while (int)(n/5) > 0:
            cnt += (int)(n/5)
            n = (int)(n/5)
        return cnt

        
if __name__ == '__main__':
    s = Solution()