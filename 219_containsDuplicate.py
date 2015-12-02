__author__ = 'feng'

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ss = set()
        h = min(len(nums), k+1)
        for n in xrange(0, h):
            if nums[n] in ss:
                return True
            ss.add(nums[n])
        if h < len(nums):
            for i in xrange(h, len(nums)):
                ss.discard(nums[i - h])
                if nums[i] in ss:
                    return True
                ss.add(nums[i])
        return False

if __name__ == '__main__':
    s = Solution()
    s.containsNearbyDuplicate([-1,-1], 1)