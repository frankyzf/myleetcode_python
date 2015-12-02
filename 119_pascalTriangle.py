__author__ = 'feng'
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex <= 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        elif rowIndex == 2:
            return [1,2,1]
        else:
            a = [1,2,1]
            for i in xrange(2, rowIndex):
                b =[ 1]
                for j in xrange(0, len(a)-1):
                    b.append(a[j] + a[j+1])
                b.append(1)
                a = b
            return a


if __name__ == '__main__':
    s = Solution()