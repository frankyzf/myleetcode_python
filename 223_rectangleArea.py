__author__ = 'feng'

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        a = (C-A) * (D-B)
        b = (G-E) * (H-F)
        if (A < E and C < E) or (E < A and G<A)  or (B< F and D < F) or (F < B and H < B):
            c = 0
        else:
            c = (min(G, C) - max(A, E)) * (min(D, H) - max(B, F))
        return a+b -c


if __name__ == '__main__':
    s = Solution()