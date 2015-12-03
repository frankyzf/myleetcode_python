__author__ = 'feng'

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ss = str.split()
        if len(pattern) == 0:
            return len(ss) == 0
        if len(pattern) != len(ss):
            return False
        m ={}
        revm = {}
        for i in xrange(0, len(pattern)):
            if pattern[i] in m:
                if m[pattern[i]] != ss[i]:
                    return False
            elif ss[i] in revm:
                if pattern[i] != revm[ss[i]]:
                    return False
            else:
                m[pattern[i]] = ss[i]
                revm[ss[i]] = pattern[i]
        return True

if __name__ == '__main__':
    s = Solution()
    print s.wordPattern("abba", "dog dog dog dog")