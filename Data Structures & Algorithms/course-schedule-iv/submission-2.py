class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)

        for prereq, crs in prerequisites:
            adj[crs].append(prereq)
        
        prereqmap = {}

        def dfs(crs):
            if crs not in prereqmap:
                prereqmap[crs] = set()
                for pre in adj[crs]:
                    prereqmap[crs].add(pre)     # direct
                    prereqmap[crs] |= dfs(pre)  # indirect

            return prereqmap[crs]

        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in prereqmap[v])
        
        return res