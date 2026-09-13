class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if (r < 0 or c < 0 or r == m or c == n or not grid[r][c] or (r, c) in visit):
                return 0
            visit.add((r, c))
            res = 1
            for dr, dc in direct:
                res += dfs(r + dr, c + dc)
            return res

        borderland, land=0, 0
        for r in range(m):
            for c in range(n):
                land+=grid[r][c]
                if (grid[r][c] and (r,c) not in visit and (c in [0, n - 1] or r in [0, m - 1])):
                    borderland+=dfs(r,c)
        
        return land-borderland