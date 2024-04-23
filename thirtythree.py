class Solution:
    def addDigits(self, num: int) -> int:
        res=0
        while(num>0):
            num1=num%10
            res+=num1
            num=int(num/10)
        return res
sol=Solution()
print(sol.addDigits(12387))