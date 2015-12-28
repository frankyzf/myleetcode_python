from util import *

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums)-1
        while i < j:
            while i < j and nums[i] == 0:
                i += 1
            while i < j and nums[j] != 0:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        k = len(nums)-1
        while j < k:
            while j <  k and nums[j] == 1:
                j += 1
            while j < k and nums[k] != 1:
                k -=1
            nums[j],nums[k] = nums[k], nums[j]


if __name__ == '__main__':
    s = Solution()
    