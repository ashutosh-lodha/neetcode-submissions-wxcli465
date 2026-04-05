class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res, l, r = 0, 0, len(heights) - 1
        maxH = max(heights)

        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            res = max(res, area)

            if heights[r] > heights[l]:
                l += 1
            else: 
                r -= 1
            if res >= maxH*(r-l):
                break
        return res
"""
        this is the main spolution above one is just optimised a little bit
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area =  (r - l) * min(heights[r], heights[l])
            res = max(area, res)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return res
"""