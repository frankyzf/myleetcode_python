__name__ = 'feng'

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = {}
        pn = 0
        while n != 1 and n not in d:
            nn = n
            d[n] = 1
            while nn > 0:
                t = (int)(nn/10)*10
                pn += (nn-t) * (nn-t)
                nn = (int)(t/10)
            n, pn = pn, 0
        return n == 1


if __name__ == '__main__':
    s = Solution()