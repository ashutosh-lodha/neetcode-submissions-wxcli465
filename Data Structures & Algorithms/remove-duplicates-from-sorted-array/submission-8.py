class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique=list(sorted(set(nums)))
        nums[:len(unique)-1]=unique
        return len(unique)