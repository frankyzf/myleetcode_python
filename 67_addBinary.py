__author__ = 'feng'

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        carry = 0
        i = -1
        res = []
        while i >= -len(a) and i >= -len(b):
            t = carry + int(a[i]) + int(b[i])
            carry = int(t >= 2)
            res.append(t%2)
            i -=1
        while i >=  -len(a):
            t = carry + int(a[i])
            carry = int(t >=2)
            res.append(t%2)
            i -= 1
        while i >= -len(b):
            t = carry + int(b[i])
            carry = int(t >=2)
            res.append(t%2)
            i -= 1
        if carry == 1:
            res.append(carry)
        res.reverse()
        st = map(lambda x: str(x), res)
        return "".join(st)

if __name__ == '__main__':
    s = Solution()
    print s.addBinary("1010", "1011")