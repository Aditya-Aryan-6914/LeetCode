class Solution(object):
    def shuffle(self, nums, n):
        output = []
        for i in range(n):
            output.append(nums[i])
            output.append(nums[i + n])
        return output