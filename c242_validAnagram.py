__name__ = 'feng'

from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        print Counter(s).items()
        return Counter(s).items() == Counter(t).items()


if __name__ == "__main__":
    print "main"
    s = Solution()
    print s.isAnagram("abc", "bac")