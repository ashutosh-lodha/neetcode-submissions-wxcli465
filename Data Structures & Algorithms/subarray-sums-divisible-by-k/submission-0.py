class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixsum = 0
        res = 0 
        remaincount = defaultdict(int)
        remaincount[0] = 1

        for n in nums:
            prefixsum+=n
            remain = prefixsum % k
            res+=remaincount[remain]
            remaincount[remain]+=1
        
        return res