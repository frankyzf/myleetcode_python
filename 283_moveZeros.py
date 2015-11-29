__name__ = 'feng'


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a = 0
        for i in xrange(0, len(nums)):
            if not nums[i] == 0:
                nums[a] = nums[i]
                a += 1
        while a < len(nums):
            nums[a] = 0
            a += 1


if __name__ == '__main__':
    s = Solution()