class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        n = len(words)
        cache = [0]*n
        res = []
        prev = 0

        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                    prev+= 1
            cache[i] = prev

        for l, r in queries:
            if l!=0:
                res.append(cache[r]-cache[l-1])
            else:
                res.append(cache[r])
        
        return res
