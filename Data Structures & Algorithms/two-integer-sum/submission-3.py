class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i,num in enumerate(nums):
            if target-num not in map:
                map[num]=i
            else:
                return [map[target-num],i]
