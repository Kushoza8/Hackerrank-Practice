class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math
        if(c==1 or c==2 or c==0):
            return True
        else:
            for i in range(math.floor(math.sqrt(c))+1):
                for j in range(math.floor(math.sqrt(c))+1):
                    if (i**2)+((j)**2)==c:
                        return True
                        break
        return False
sol=Solution()
print(sol.judgeSquareSum(9999999999))
