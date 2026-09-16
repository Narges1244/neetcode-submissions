class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_unit = 0
        while left < right:
            h = min(heights[left], heights[right])
            a = h * (right - left)
            max_unit = max(max_unit, a)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_unit