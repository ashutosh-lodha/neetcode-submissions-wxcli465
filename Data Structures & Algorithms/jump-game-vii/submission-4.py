class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        if s[n-1] == '1':
            return False

        dp = [False]*n
        dp[0] = True
        
        for i in range(n):
            if not dp[i]:
                continue
            
            l = i + minJump
            r = min(i + maxJump, n-1)

            for j in range(l, r + 1):
                if s[j] == '0':
                    dp[j] = True

        return dp[n-1]