class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        res = []
        p_count = [0] * 26
        s_count = [0] * 26

        for i in range(len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1
        
        if p_count == s_count:
            res.append(0)
        
        for right in range(len(p), len(s)):
            #char entering
            s_count[ord(s[right]) - ord('a')] += 1

            #char leaving
            left = right - len(p)
            s_count[ord(s[left]) - ord('a')] -= 1

            if p_count == s_count:
                res.append(left + 1)
            
        return res
