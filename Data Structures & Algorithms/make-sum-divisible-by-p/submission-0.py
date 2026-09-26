class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remain = sum(nums) % p

        if remain == 0:
            return 0

        prefix = {0: -1}
        curr = 0
        res = len(nums)

        for i, num in enumerate(nums):
            curr = (curr + num) % p
            target = (curr - remain) % p

            if target in prefix:
                res = min(res, i - prefix[target])

            prefix[curr] = i

        return -1 if res == len(nums) else res