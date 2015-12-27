from util import *


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []
        if n <=0:
            return res
        res.append([])
        for i in range(0,n):
            for a in res:
                a.append('(')
            import copy
            aa = copy.deepcopy(res)
            for a in aa:
                a.append(')')
            res.extend(aa)
        res1 = set()
        for a in res:
            while len(a) < n*2:
                a.append(')')
            res1.add(''.join(a))
        return list(res1)



if __name__ == '__main__':
    s = Solution()
    print s.generateParenthesis(3)
    