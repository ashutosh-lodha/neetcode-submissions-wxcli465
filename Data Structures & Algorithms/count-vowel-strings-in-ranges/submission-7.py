class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        
        prefix = [0]*(len(words)+1)

        count = 0
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                    count+= 1
            prefix[i+1] = count

        res = []
        for l, r in queries:
                res.append(prefix[r+1]-prefix[l])
        
        return res
