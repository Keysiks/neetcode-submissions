class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxx = (r - l) * min(heights[l], heights[r])
        while l != r:
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            maxx = max((r - l) * min(heights[l], heights[r]), maxx)
        return maxx

