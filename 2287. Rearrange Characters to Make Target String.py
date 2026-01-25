class Solution:
    def rearrangeCharacters(self, s, target):
        from collections import Counter
        
        count_s = Counter(s)
        count_t = Counter(target)
        
        ans = float('inf')
        for ch in count_t:
            ans = min(ans, count_s[ch] // count_t[ch])
        
        return ans