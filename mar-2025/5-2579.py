class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        
        i = 1
        res = 1
        while i < n:
            res += i * 4
            i += 1
        
        return res
