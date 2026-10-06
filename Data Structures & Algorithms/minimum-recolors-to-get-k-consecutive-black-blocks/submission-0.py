class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = 0
        for i in range(k):
            if blocks[i]=="W":
                w+=1
        
        res = w
        for i in range(k, len(blocks)):
            if blocks[i-k]=="W":
                w-=1
            if blocks[i]=="W":
                w+=1
            res = min(res, w)
        
        return res
