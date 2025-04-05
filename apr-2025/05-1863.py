class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # backtrack

        def subset(idx, currXor):
            res = currXor
            for i in range(idx + 1, len(nums)):
                nextXor = currXor ^ nums[i]
                res += subset(i, nextXor)
            
            return res
        
        res = 0
        for i in range(len(nums)):
            res += subset(i, nums[i])
        
        return res
