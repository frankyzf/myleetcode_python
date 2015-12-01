__author__ = 'feng'
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows ==2:
            return [[1], [1,1]]
        r = [[1],[1,1]]
        for i in xrange(3, numRows+1):
            e = r[len(r)-1]
            cc = [1]
            for j in xrange(1, i-1):
                cc.append(e[j-1] + e[j])
            cc.append(1)
            r.append(cc)
        return r

if __name__ == '__main__':
    s = Solution()
    a = s.generate(5)
    print a