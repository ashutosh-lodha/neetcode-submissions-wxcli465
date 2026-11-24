class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        s = list(s)
        i = 0
        while i < len(s):
            if s[i] != ' ':
                j = i
                while j < len(s) and s[j] != ' ':
                    j += 1
                reverse(i, j - 1)
                i = j + 1
        return ''.join(s)
