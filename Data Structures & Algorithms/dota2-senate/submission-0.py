class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D, R = deque(), deque()
        n = len(senate)

        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append (i)

        
        while D and R:
            ri = R.popleft()
            di = D.popleft()

            if ri < di:
                R.append(ri+n)
            else:
                D.append(di+n)
        
        return "Radiant" if R else "Dire"