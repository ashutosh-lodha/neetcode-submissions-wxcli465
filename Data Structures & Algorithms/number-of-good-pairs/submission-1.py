class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        count = defaultdict(int)

        for num in nums:
            res+=count[num]
            count[num]+=1
        
        return res
        