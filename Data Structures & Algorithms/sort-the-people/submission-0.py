class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res =[]
        hton = {}

        for h, n in zip(heights, names):
            hton[h] = n
        
        for h in reversed(sorted(heights)):
            res.append(hton[h])

        return res