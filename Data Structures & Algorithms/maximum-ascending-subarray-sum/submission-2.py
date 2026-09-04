class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxsum = cursum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                cursum = 0
            cursum = cursum + nums[i]
            maxsum=max(cursum, maxsum)
        
        return maxsum