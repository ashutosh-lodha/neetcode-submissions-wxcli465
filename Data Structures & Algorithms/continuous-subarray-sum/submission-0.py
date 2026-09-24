class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remToIndex = { 0:-1 }
        total = 0

        for i, n in enumerate(nums):
            total+=n
            rem = total%k

            if rem not in remToIndex:
                remToIndex[rem] = i
            else:
                if i - remToIndex[rem]>1:
                    return True
        
        return False