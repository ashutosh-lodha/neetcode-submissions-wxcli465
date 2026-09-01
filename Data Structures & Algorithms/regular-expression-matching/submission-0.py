class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)  # Length of string and pattern
        cache = {}  # Store already computed (i, j) results

        def dfs(i, j):
            if j == n:
                return i == m

            if (i, j) in cache:
                return cache[(i, j)]

            match = i < m and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < n and p[j + 1] == "*":
                # Option 1: Skip "character*"
                # Option 2: Use current character
                cache[(i, j)] = (dfs(i, j + 2) or (match and dfs(i + 1, j)))
                return cache[(i, j)]

            if match:                               # Normal character match
                cache[(i, j)] = dfs(i + 1, j + 1)   # Move forward in both string and pattern
                return cache[(i, j)]

            # Characters don't match
            cache[(i, j)] = False
            return False

        return dfs(0, 0)