__name__ = 'feng'
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = m[s[0]]
        for i in xrange(1, len(s)):
            if m[s[i]] > m[s[i-1]]:
                n += m[s[i]] - 2*m[s[i-1]]
            else:
                n += m[s[i]]
        return n
if __name__ == '__main__':
    s = Solution()