__author__ = 'feng'

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n == 0:
            return
        res = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        while i < m:
            res.append(nums1[i])
            i += 1
        while j < n:
            res.append(nums2[j])
            j += 1
        nums1 = res

if __name__ == '__main__':
    s = Solution()
    s.merge([1], 1, [], 0)