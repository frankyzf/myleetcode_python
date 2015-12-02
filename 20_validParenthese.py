__author__ = 'feng'

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        for c in s:
            if c == ']':
                if len(st) > 0 and st[-1] == '[':
                    st.pop()
                else:
                    return False
            elif c == '}':
                if len(st) > 0 and st[-1] == '{':
                    st.pop()
                else:
                    return False
            elif c ==  ')':
                if len(st) > 0 and st[-1] == '(':
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        return len(st) == 0



if __name__ == '__main__':
    s = Solution()