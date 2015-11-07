__author__ = 'feng'


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag =list(map(lambda x: [False, x], xrange(0, 128)))
        r = 0
        l = 0
        low = -1
        for i in range(0, len(s)):
            c = ord(s[i])
            if flag[c][0]:
                h = flag[c][1]
                if low >= h:
                    l +=1
                else:
                    l = i - h
                    low = h
            else:
                l += 1

            if l > r:
                r = l
            flag[c][0] = True
            flag[c][1] = i
        return r

if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring("abcabc")
