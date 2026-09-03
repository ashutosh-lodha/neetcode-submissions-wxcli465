class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxr = -1

        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = maxr
            maxr = max(maxr, temp)
        
        return arr

