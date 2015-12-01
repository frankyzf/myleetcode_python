__author__ = 'feng'

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 1
        while j < len(nums) and nums[j-1] != nums[j]:
            j += 1
        if j == len(nums):
            return j
        i = j
        for j in xrange(i+1, len(nums)):
            if nums[i] != nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


if __name__ == '__main__':
    s = Solution()