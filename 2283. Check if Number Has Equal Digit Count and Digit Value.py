class Solution:
    def digitCount(self, num):
        from collections import Counter
        
        freq = Counter(num)
        
        for i in range(len(num)):
            if freq.get(str(i), 0) != int(num[i]):
                return False
        
        return True