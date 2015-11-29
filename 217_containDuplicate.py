__name__ = 'feng'

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in xrange(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

if __name__ == '__main__':
    s = Solution()