class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h, n = len(haystack), len(needle)
        for i in range(h-n+1):
           if haystack[i]==needle[0]:
            j= 0
            while j<n:
                if haystack[i+j]!=needle[j]:
                    i+=j-1
                    break
                j+=1
                if j==n:
                    return i
        return -1