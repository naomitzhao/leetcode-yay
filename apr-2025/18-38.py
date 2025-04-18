class Solution:
    def countAndSay(self, n: int) -> str:
        # brute force recursion

        if n == 1:
            return "1"
        
        prevRes = self.countAndSay(n - 1)

        res = []

        currNum = None
        currCount = 0
        for num in prevRes:
            if not currNum:
                currNum = num
                currCount = 1
            elif num == currNum:
                currCount += 1
            else:
                res.append(str(currCount))
                res.append(str(currNum))
                currNum = num
                currCount = 1
        
        res.append(str(currCount))
        res.append(str(currNum))
    
        return ''.join(res)
