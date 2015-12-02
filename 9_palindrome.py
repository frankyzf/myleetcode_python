__author__ = 'feng'

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        h = 1
        x1 = x
        while x1:
            h *= 10
            x1 /= 10
        h /= 10
        while h >= 10:
            if (int)(x/h) != x%10:
                return False
            x  -= (int)(x/h)*h
            x /=10
            h /= 100
        return True



if __name__ == '__main__':
    s = Solution()
    print s.isPalindrome(10)