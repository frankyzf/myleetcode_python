__author__ = 'feng'


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            d = 0
            n = num
            while n > 0:
                t = (int)(n/10)
                d += n - 10*t
                n = t
            num = d
        return num

if __name__ == '__main__':
    s = Solution()
    print s.addDigits(10)