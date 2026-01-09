def divideArray(self,nums):
    d={}
    for i in nums:
        if i not in d:
            d[i] =1
        else:
            d[i] +=1
            
    for j in d.values():
        if j % 2 != 0:
            return False
    return True

        