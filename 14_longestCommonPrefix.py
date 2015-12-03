__author__ = 'feng'
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if len(strs) == 0:
            return prefix
        for i in xrange(0, len(strs[0])):
            c = strs[0][i]
            b = True
            for j in xrange(1,len(strs)):
                if i >= len(strs[j]) or c != strs[j][i]:
                    b = False
                    break
            if b:
                prefix += c
            else:
                break
        return prefix

if __name__ == '__main__':
    s = Solution()