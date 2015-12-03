__author__ = 'feng'

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        from collections import Counter
        s = '1'
        while n > 1:
            i = 0
            ns = ""
            while i < len(s):
                c = s[i]
                j = 1
                i += 1
                while i < len(s) and s[i] == c:
                    j += 1
                    i += 1
                ns += str(j) + c
            s = ns
            n -= 1
        return s




if __name__ == '__main__':
    s = Solution()
    print s.countAndSay(5)