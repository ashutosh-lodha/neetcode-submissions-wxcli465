class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        prefixSum = 0
        res=0

        for i in range(0, len(nums)-1):
            prefixSum+=nums[i]
            if prefixSum>=(totalSum-prefixSum):
                res+=1
        
        return res


