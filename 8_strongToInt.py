__author__ = 'feng'

from util import *
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        value = 0
        i = 0
        b = None
        while i < len(str) and str[i] == " ":
             i += 1
        while i < len(str) and (str[i] == "-" or str[i] == "+"):
            if i < len(str) and str[i] == "-":
                if b != None:
                    return 0
                b = False
                i+= 1
            if i < len(str) and str[i] == "+":
                if b != None:
                    return 0
                b = True
                i += 1
        while i < len(str):
            if not str[i].isdigit():
                break
            value *= 10
            value += int(str[i])
            i += 1
        if b == False:
            value *=-1
            if value < -2147483648:
                return -2147483648
            return value
        else:
            if value > 2147483647:
                return 2147483647
            return value



if __name__ == '__main__':
    s = Solution()
    print s.myAtoi("  -0012a42")