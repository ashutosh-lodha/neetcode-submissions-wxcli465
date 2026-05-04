class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        # STEP 1: Build LCS table
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):

                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        # STEP 2: Recover LCS string
        i, j = n, m
        lcs = []

        while i > 0 and j > 0:

            if str1[i - 1] == str2[j - 1]:
                lcs.append(str1[i - 1])
                i -= 1
                j -= 1

            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        lcs.reverse()
        lcs = "".join(lcs)

        # STEP 3: Build shortest common supersequence
        i = j = 0
        ans = []

        for c in lcs:

            while str1[i] != c:
                ans.append(str1[i])
                i += 1

            while str2[j] != c:
                ans.append(str2[j])
                j += 1

            ans.append(c)
            i += 1
            j += 1

        # remaining chars
        ans.append(str1[i:])
        ans.append(str2[j:])

        return "".join(ans)