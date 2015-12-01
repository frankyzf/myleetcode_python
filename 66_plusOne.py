__author__ = 'feng'

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return [1]
        for j in xrange(len(digits)-1, -1, -1):
            if digits[j] != 9:
                break
        c = []
        if j < len(digits) -1:
            c.extend(map(lambda x: 0, digits[j+1:]))

        if j == 0:
            if digits[0] == 9:
                c.insert(0, 0)
                c.insert(0, 1)
            else:
                c.insert(0, digits[0]+1)
        else:
            c.insert(0, digits[j]+1)
            for k in xrange(j-1,-1,-1):
                c.insert(0, digits[k])

        return c


if __name__ == '__main__':
    s = Solution()
    a = s.plusOne([1,0])
    print a