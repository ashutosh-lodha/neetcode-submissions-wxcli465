class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node, parent):
            time =  0

            for child in adj[node]:
                if child == parent:
                    continue

                childtime = dfs(child, node)
                if childtime>0 or hasApple[child]:
                    time+=2+childtime
            return time
        
        return dfs(0, -1)

