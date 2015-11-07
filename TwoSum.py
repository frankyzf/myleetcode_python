__author__ = 'feng'

import operator

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        index = range(0, len(nums))
        snums = zip(index, nums)
        snums = sorted(snums, key=operator.itemgetter(1))
        i = 0
        j = len(snums)-1
        while(i < j):
            if snums[i][1] + snums[j][1] < target:
                i +=1
            elif snums[i][1] + snums[j][1] > target:
                j -=1
            else:
                res.append(snums[i][0]+1)
                res.append(snums[j][0]+1)
                break
        res = sorted(res)
        return res

if __name__ == '__main__':
    print Solution().twoSum([3,2,4], 6)