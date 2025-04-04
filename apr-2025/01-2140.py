class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def getMaxPoints(questions, idx):
            if idx >= len(questions):
                return 0
            
            if dp[idx] != -1:
                return dp[idx]
            
            dp[idx] = max(getMaxPoints(questions, idx + 1), getMaxPoints(questions, idx + questions[idx][1] + 1) + questions[idx][0])
            return dp[idx]
        
        dp = [-1] * len(questions)
        res = getMaxPoints(questions, 0)
        return res
        
        
