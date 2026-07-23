class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        g = 0
        maxi = 0
        for i in nums:
            if i == 1:
                maxi = maxi + 1
            else:
                g = max(g,maxi)
                maxi = 0
        return max(g,maxi)
