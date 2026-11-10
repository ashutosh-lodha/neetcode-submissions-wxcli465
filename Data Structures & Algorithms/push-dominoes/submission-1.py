class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list('L' + dominoes + 'R')

        prev = 0

        for curr in range(1, len(dom)):
            if dom[curr] == '.':
                continue

            if dom[prev] == dom[curr]:
                for i in range(prev + 1, curr):
                    dom[i] = dom[prev]

            elif dom[prev] == 'R' and dom[curr] == 'L':
                l, r = prev + 1, curr - 1

                while l < r:
                    dom[l] = 'R'
                    dom[r] = 'L'
                    l += 1
                    r -= 1

            prev = curr

        return ''.join(dom[1:-1])
