class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r, m = 0, n-1, 0
        while l < r:
            area = (r - l) * min(height[r],height[l])
            m = max(area,m)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return m