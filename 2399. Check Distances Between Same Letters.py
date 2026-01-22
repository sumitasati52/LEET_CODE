class Solution:
    def checkDistances(self, s, distance):
        first_pos = {}
        
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            
            if ch in first_pos:
                if i - first_pos[ch] - 1 != distance[idx]:
                    return False
            else:
                first_pos[ch] = i
        
        return True