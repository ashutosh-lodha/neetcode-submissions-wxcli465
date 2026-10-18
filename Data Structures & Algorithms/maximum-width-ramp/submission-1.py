class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []

        for i, x in enumerate(nums):
            if not stack or x<nums[stack[-1]]:
                stack.append(i)
        res = 0

        for i in range(len(nums) -1, -1, -1):
            while stack and nums[stack[-1]]<=nums[i]:
                res=max(res, i-stack.pop())
        
        return res
