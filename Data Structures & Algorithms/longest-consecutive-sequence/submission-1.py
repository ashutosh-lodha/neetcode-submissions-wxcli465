class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0
        
        for num in nums:
            #CHECK IF ITS NOT THE STARTING OF A SEQUENCE - BY CHECKING PREVIOUS NUMBER EXISTS IN THE SET 
            if (num-1) not in numSet:
                length = 0
                while (num+length) in numSet:
                    length+=1
                longest=max(length, longest)

        return longest  
