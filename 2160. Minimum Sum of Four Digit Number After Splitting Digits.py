class Solution(object):
    def minimumSum(self, num):
        a=list(str(num))
        a.sort()
        n1= int(a[0])*10+int(a[-1])
        n2=int(a[1])*10+int(a[-2])
        return n1 + n2  