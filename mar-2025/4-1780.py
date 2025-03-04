class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        fac = 3

        while fac * 3 <= n:
            fac *= 3
        
        while fac >= 1:
            if n >= fac:
                n -= fac
            fac /= 3
        
        if n == 0:
            return True
        
        return False
