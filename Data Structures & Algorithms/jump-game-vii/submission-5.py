class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        if s[n - 1] == '1':
            return False

        dp = [False] * n
        dp[0] = True

        reachable = 0

        for i in range(1, n):

            # Add the new position entering the window
            if i - minJump >= 0 and dp[i - minJump]:
                reachable += 1

            # Remove the old position leaving the window
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                reachable -= 1

            if s[i] == '0' and reachable > 0:
                dp[i] = True

        return dp[n - 1]