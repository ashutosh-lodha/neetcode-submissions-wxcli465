class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid), len(obstacleGrid[0])
        row=[0]*n
        row[n-1]=1

        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if obstacleGrid[r][c]:
                    row[c]=0
                elif c+1<n:
                    row[c]=row[c]+row[c+1]
        return row[0]
        