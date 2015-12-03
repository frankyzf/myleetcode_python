__author__ = 'feng'

from util import *
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i  = 0
        j = len(s) -1
        while i < j:
            if not s[i].isalnum() or s[i] == " ":
                i += 1
            elif not s[j].isalnum() or s[j] == " ":
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True


if __name__ == '__main__':
    s = Solution()