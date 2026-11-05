class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        numse = defaultdict(int)
        for num in nums:
            numse[num] += 1
        for item in numse.values():
            if item % 2 != 0:
                return False
        return True