class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        index = {}

        res = -1

        for i, c in enumerate(s):
            if c in index:
                res = max(res, i - index[c] - 1)
            else:
                index[c] = i
        
        return res