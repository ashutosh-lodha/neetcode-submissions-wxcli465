class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0 
        slen, tlen = len(s), len(t)
        while i<slen and j<tlen:
            if s[i] == t[j]:
                j+=1
            i+=1
        return len(t[j:])