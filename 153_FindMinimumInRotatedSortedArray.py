from util import *


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start < end:
            mid = (start+end)//2
            if nums[start] > nums[end]:
                if nums[mid] <= nums[end]:
                    end = mid
                else:
                    start = mid +1
            else:
                end = mid

        return nums[start]

if __name__ == '__main__':
    s = Solution()
    print s.findMin([4,5,6,7,0,1,2])
    