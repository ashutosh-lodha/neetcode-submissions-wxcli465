class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        subset=[]

        def dfs(i):
            if i >=len(nums):
                res.append(subset.copy())
                return
            # for the left side - including the element
            subset.append(nums[i])
            dfs(i+1)

            # for the right side - not including the element
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res