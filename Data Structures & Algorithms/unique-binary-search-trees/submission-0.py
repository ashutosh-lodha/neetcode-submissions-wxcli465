class Solution:
    def numTrees(self, n: int) -> int:
        res = 1
        for i in range(n):
            res *= (4 * i + 2) / (i + 2)
        return int(res)
