class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        q = deque(s)
        for i,c in enumerate(s):
            if count[c]==-1:
                q.popleft()
                continue
            if count[c]>1:
                q.popleft()
                count[c]=-1
            else:
                return i
        return -1
