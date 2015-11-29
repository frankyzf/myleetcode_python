__author__ = 'feng'


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1+ len2)%2:
            return self.findnum(nums1, nums2, 0, len1, 0, len2, (len1+len2+1)/2-1)
        else:
            t1 = (len1+len2)/2 -1
            t2 = (len1+len2)/2
            return (self.findnum(nums1, nums2, 0, len1, 0, len2, t1) + self.findnum(nums1, nums2, 0, len1, 0, len2, t2))/2.0

    def findnum(self, nums1, nums2, start1, len1, start2, len2, index):
        if len1 == 0:
            return nums2[start2+index]
        elif len2 == 0:
            return nums1[start1+index]
        elif index == 0:
            if nums1[0] < nums2[0]:
                return nums1[0]
            else:
                return nums2[0]
        elif index == len1+len2-1:
            if nums1[start1+len1-1] > nums2[start2+len2-1]:
                return nums1[start1+len1-1]
            else:
                return nums2[start2+len2-1]
        else:
            m1 = len1/2
            m2 = len2/2
            if index <= m1+m2+1:#lower part
                if nums1[m1] < nums2[m2]:
                    return self.findnum(nums1, nums2, start1, len1, start2, m2, index)
                else:
                    return self.findnum(nums1, nums2, start1, m1, start2, len2, index)
            else:
                if nums1[m1] < nums2[m2]:
                    return self.findnum(nums1, nums2, start1+m1+1, len1-m1-1, start2, len2, index - m1-1)
                else:
                    return self.findnum(nums1, nums2, start1, len1, start2+m2+1, len2-m2-1, index -m2-1)

if __name__ == "__main__":
    print Solution().findMedianSortedArrays([3],[1,2,4])