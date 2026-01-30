class Solution:
    def removeDigit(self, number, digit):
        res = "0"
        
        for i in range(len(number)):
            if number[i] == digit:
                candidate = number[:i] + number[i+1:]
                res = max(res, candidate)
        
        return res
