__author__ = 'feng'
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in xrange(0, len(nums)):
            if not nums[j] == val:
                nums[i] = nums[j]
                i += 1
        del nums[i:]
        return len(nums)

if __name__ == '__main__':
    s = Solution()