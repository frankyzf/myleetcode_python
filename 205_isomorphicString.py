__author__ = 'feng'

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return len(t) == 0
        m = {}
        rm = {}
        for i in xrange(0, len(s)):
            if s[i] in m:
                if m[s[i]] != t[i]:
                    return False
            elif t[i] in rm:
                if rm[t[i]] != s[i]:
                    return False
            else:
                rm[t[i]] = s[i]
                m[s[i]] = t[i]
        return True



if __name__ == '__main__':
    s = Solution()