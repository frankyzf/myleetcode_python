__name__ = 'feng'
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = 0
        cnt = 0
        for n in nums:
            if cnt == 0:
                t = n
                cnt += 1
            elif t == n:
                cnt += 1
            else:
                cnt -= 1
        return t

if __name__ == '__main__':
    s = Solution()