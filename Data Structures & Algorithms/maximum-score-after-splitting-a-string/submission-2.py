class Solution:
    def maxScore(self, s: str) -> int:
        totalzero, totalone, res = 0, 0, 0
        for c in s:
            if c=='0':
                totalzero+=1
            else:
                totalone+=1
        leftzero, leftone=0, 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                leftzero+=1
            else:
                leftone+=1
            res=max(res, leftzero+(totalone-leftone))
        return res