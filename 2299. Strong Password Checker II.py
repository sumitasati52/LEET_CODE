class Solution:
    def strongPasswordCheckerII(self, password):
        if len(password) < 8:
            return False
        
        lower = upper = digit = special = False
        specials = "!@#$%^&*()-+"
        
        for i in range(len(password)):
            ch = password[i]
            
            if ch.islower():
                lower = True
            elif ch.isupper():
                upper = True
            elif ch.isdigit():
                digit = True
            elif ch in specials:
                special = True
            
            if i > 0 and password[i] == password[i - 1]:
                return False
        
        return lower and upper and digit and special