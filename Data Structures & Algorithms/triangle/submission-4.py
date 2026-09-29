class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n==1:
            return triangle[0][0]

        dp = triangle[-1]

        for arr in triangle[-2::-1]:
            for i in range(len(arr)):
                dp[i]=arr[i] + min(dp[i], dp[i+1])
            print(dp)
        
        return dp[0]
                