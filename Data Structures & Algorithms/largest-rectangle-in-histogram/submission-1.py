class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0
        for i ,h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                h2,j = stack.pop()
                w = i - j
                a = h2* w 
                max_area = max(max_area, a)
                start = j
            stack.append((h,start))
        while stack:
            h,j = stack.pop()
            w = n - j
            max_area = max(max_area, w*h) 
        return max_area