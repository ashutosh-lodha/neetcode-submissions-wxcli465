class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        
        prefix = [0]*len(words)

        count = 0
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                    count+= 1
            prefix[i] = count

        res = []
        for l, r in queries:
            if l!=0:
                res.append(prefix[r]-prefix[l-1])
            else:
                res.append(prefix[r])
        
        return res
