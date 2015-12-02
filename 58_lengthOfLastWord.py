__author__ = 'feng'
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = s.split()
        if len(a):
            return len(a[len(a)-1])
        return 0

if __name__ == '__main__':
    s = Solution()