class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        heapq.heapify(minHeap)
        for p in points:
            distance=(0-p[0])**2+(0-p[1])**2
            heapq.heappush(minHeap, (distance, p))

        res=[]
        for _ in range(k):
            top=heapq.heappop(minHeap)
            res.append(top[1])
        return res