class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countgap = defaultdict(int)

        for r in wall:
            total = 0
            for i in range(len(r)-1):
                total += r[i]
                countgap[total] += 1
        
        return len(wall) - max(countgap.values(), default=0)