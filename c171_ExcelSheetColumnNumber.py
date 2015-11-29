__name__ = 'feng'
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = 0
        for ch  in s:
            a = a*26 + ord(ch) - ord('A') +1
        return a


if __name__ == '__main__':
    s = Solution()