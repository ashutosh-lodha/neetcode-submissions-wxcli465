class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}
        answer = 0
        for w, h in rectangles:
            count[w/h]=1+count.get(w/h, 0)
        for c in count.values():
            if c >0:
                answer += (c*(c-1))//2
        return answer
